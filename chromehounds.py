"""
Chromehounds Information Plugin for Logamus Bot.
This plugin provides comprehensive information about the Chromehounds game including lore, mechanics, parts, and strategies.
"""
import discord
from discord import app_commands
from discord.ext import commands
import logging
from typing import List, Dict, Optional
import asyncio
import re

from plugins import Plugin
from .data import (
    LORE_DATA,
    ROLE_TYPES,
    EQUIPMENT_DATA,
    COMBAT_SYSTEMS,
    NATIONS_DATA,
    ORGANIZATIONS_DATA,
    HISTORICAL_DATA,
    COMMUNICATION_DATA,
    ONLINE_FEATURES,
    TECHNICAL_DATA,
    LEGACY_DATA,
    MECHANICS_DATA,
    search_chromehounds_data,
    get_quick_suggestions
)

class ChromehoundsInfo(Plugin):
    """Plugin for providing Chromehounds game information."""
    
    name = "chromehounds_info"
    description = "Comprehensive information tool for the Chromehounds game"
    version = "1.0.0"
    
    def __init__(self, bot):
        super().__init__(bot)
        self.logger = logging.getLogger(f"plugins.{self.name}")
        
    async def setup(self):
        """Set up the plugin."""
        self.logger.info("Setting up Chromehounds Information plugin...")

    @app_commands.command(
        name="chromehounds",
        description="Search for information about Chromehounds"
    )
    @app_commands.describe(
        command="Command type (search/lore/mechanics/parts/strategy)",
        topic="Topic to search for or get information about"
    )
    async def chromehounds_command(
        self,
        interaction: discord.Interaction,
        command: str,
        topic: Optional[str] = None
    ):
        """Main command handler for Chromehounds information."""
        await interaction.response.defer()
        
        command = command.lower()
        
        if command == "search":
            if not topic:
                suggestions = get_quick_suggestions()
                embed = discord.Embed(
                    title="Chromehounds Search",
                    description="Please provide a search term. Here are some suggested topics:",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Suggested Topics",
                    value="\n".join(f"• {topic}" for topic in suggestions[:10]),
                    inline=False
                )
            else:
                results = search_chromehounds_data(topic)
                if not results:
                    suggestions = get_quick_suggestions()
                    embed = discord.Embed(
                        title="No Results Found",
                        description=f"No results found for '{topic}'. Here are some suggested topics:",
                        color=discord.Color.blue()
                    )
                    embed.add_field(
                        name="Suggested Topics",
                        value="\n".join(f"• {s}" for s in suggestions[:5]),
                        inline=False
                    )
                else:
                    embed = discord.Embed(
                        title=f"Search Results: {topic}",
                        color=discord.Color.blue()
                    )
                    for result in results:
                        embed.add_field(
                            name=result["title"],
                            value=result["content"][:1024] if "content" in result else result["description"][:1024],
                            inline=False
                        )
        
        elif command == "lore":
            # Handle lore command with more flexible topic matching
            if not topic:
                embed = self.create_category_overview("Lore & Background", LORE_DATA)
            else:
                results = self.search_category(topic, LORE_DATA, NATIONS_DATA, ORGANIZATIONS_DATA, HISTORICAL_DATA)
                embed = self.create_search_results(results, "Lore", topic)
        
        elif command == "mechanics":
            # Handle mechanics command with expanded data
            if not topic:
                embed = self.create_category_overview("Game Mechanics", MECHANICS_DATA)
            else:
                results = self.search_category(topic, MECHANICS_DATA, COMBAT_SYSTEMS, COMMUNICATION_DATA)
                embed = self.create_search_results(results, "Mechanics", topic)
        
        elif command == "parts":
            # Handle parts command with comprehensive equipment data
            if not topic:
                embed = self.create_category_overview("Parts & Equipment", EQUIPMENT_DATA)
            else:
                results = self.search_category(topic, EQUIPMENT_DATA, ROLE_TYPES)
                embed = self.create_search_results(results, "Parts", topic)
        
        elif command == "strategy":
            # Handle strategy command with tactical information
            if not topic:
                embed = self.create_category_overview("Strategy & Tactics", ROLE_TYPES)
            else:
                results = self.search_category(topic, ROLE_TYPES, COMBAT_SYSTEMS)
                embed = self.create_search_results(results, "Strategy", topic)
        
        else:
            embed = discord.Embed(
                title="Invalid Command",
                description="Please use: search, lore, mechanics, parts, or strategy",
                color=discord.Color.red()
            )
        
        await interaction.followup.send(embed=embed)

    def create_category_overview(self, title: str, data: dict) -> discord.Embed:
        """Create an overview embed for a category."""
        embed = discord.Embed(
            title=title,
            color=discord.Color.blue()
        )
        
        # Add available topics
        topics = []
        for key, value in data.items():
            if isinstance(value, dict) and "title" in value:
                topics.append(value["title"])
            else:
                topics.append(key.replace("_", " ").title())
        
        embed.add_field(
            name="Available Topics",
            value="\n".join(f"• {topic}" for topic in topics),
            inline=False
        )
        
        return embed

    def search_category(self, topic: str, *data_sources: dict) -> List[dict]:
        """Search within specific categories for matching information."""
        results = []
        topic = topic.lower()
        
        for data_source in data_sources:
            for key, value in data_source.items():
                if isinstance(value, dict):
                    # Check title matches
                    if "title" in value and topic in value["title"].lower():
                        results.append(value)
                    # Check content/description matches
                    elif "content" in value and topic in value["content"].lower():
                        results.append(value)
                    elif "description" in value and topic in value["description"].lower():
                        results.append(value)
                    
                    # Search in nested dictionaries
                    for subkey, subvalue in value.items():
                        if isinstance(subvalue, (str, list)):
                            content = str(subvalue).lower()
                            if topic in content and value not in results:
                                results.append(value)
                                break
        
        return results[:5]  # Return top 5 results

    def create_search_results(self, results: List[dict], category: str, topic: str) -> discord.Embed:
        """Create an embed for search results."""
        if not results:
            embed = discord.Embed(
                title=f"No {category} Results",
                description=f"No results found for '{topic}' in {category}. Try using broader terms or check the category overview.",
                color=discord.Color.blue()
            )
        else:
            embed = discord.Embed(
                title=f"{category} Information: {topic}",
                color=discord.Color.blue()
            )
            
            for result in results:
                embed.add_field(
                    name=result["title"],
                    value=result["content"][:1024] if "content" in result else result["description"][:1024],
                    inline=False
                )
        
        return embed

    @app_commands.command(
        name="hound_role",
        description="Get information about a specific HOUND role type"
    )
    @app_commands.describe(
        role="The HOUND role type (soldier, sniper, defender, scout, heavy_gunner, commander)"
    )
    async def hound_role(
        self,
        interaction: discord.Interaction,
        role: str
    ):
        """Get detailed information about a specific HOUND role type."""
        role = role.lower()
        
        if role not in ROLE_TYPES:
            embed = discord.Embed(
                title="Invalid Role Type",
                description="Please choose from: soldier, sniper, defender, scout, heavy_gunner, commander",
                color=discord.Color.red()
            )
        else:
            role_data = ROLE_TYPES[role]
            embed = discord.Embed(
                title=f"HOUND Role: {role_data['title']}",
                description=role_data['description'],
                color=discord.Color.blue()
            )
            
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="equipment",
        description="Get information about HOUND equipment and parts"
    )
    @app_commands.describe(
        category="Equipment category (weapons, mobility, support)"
    )
    async def equipment(
        self,
        interaction: discord.Interaction,
        category: str
    ):
        """Get information about HOUND equipment and parts."""
        category = category.lower()
        
        if category not in EQUIPMENT_DATA:
            embed = discord.Embed(
                title="Invalid Equipment Category",
                description="Please choose from: weapons, mobility, support",
                color=discord.Color.red()
            )
        else:
            embed = discord.Embed(
                title=f"HOUND Equipment: {category.title()}",
                color=discord.Color.blue()
            )
            
            data = EQUIPMENT_DATA[category]
            for subcategory, items in data.items():
                embed.add_field(
                    name=subcategory.replace('_', ' ').title(),
                    value="\n".join(f"• {item}" for item in items),
                    inline=False
                )
                
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="mechanics",
        description="Get information about game mechanics"
    )
    @app_commands.describe(
        aspect="Game mechanic aspect (combat, customization, damage)"
    )
    async def mechanics(
        self,
        interaction: discord.Interaction,
        aspect: str
    ):
        """Get information about specific game mechanics."""
        aspect = aspect.lower()
        
        if aspect not in MECHANICS_DATA:
            embed = discord.Embed(
                title="Invalid Mechanic Aspect",
                description="Please choose from: combat, customization, damage",
                color=discord.Color.red()
            )
        else:
            mechanic_data = MECHANICS_DATA[aspect]
            embed = discord.Embed(
                title=mechanic_data['title'],
                description=mechanic_data['content'],
                color=discord.Color.blue()
            )
            
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="communication",
        description="Get information about communication systems"
    )
    @app_commands.describe(
        system="Communication system (combas, network_areas, commander_systems)"
    )
    async def communication(
        self,
        interaction: discord.Interaction,
        system: str
    ):
        """Get information about communication systems."""
        system = system.lower()
        
        if system not in COMMUNICATION_DATA:
            embed = discord.Embed(
                title="Invalid Communication System",
                description="Please choose from: combas, network_areas, commander_systems",
                color=discord.Color.red()
            )
        else:
            system_data = COMMUNICATION_DATA[system]
            embed = discord.Embed(
                title=system_data['title'],
                description=system_data['content'],
                color=discord.Color.blue()
            )
            
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="online",
        description="Get information about online features"
    )
    @app_commands.describe(
        feature="Online feature (neroimus_war, squad_mechanics, territory_control)"
    )
    async def online(
        self,
        interaction: discord.Interaction,
        feature: str
    ):
        """Get information about online features."""
        feature = feature.lower()
        
        if feature not in ONLINE_FEATURES:
            embed = discord.Embed(
                title="Invalid Online Feature",
                description="Please choose from: neroimus_war, squad_mechanics, territory_control",
                color=discord.Color.red()
            )
        else:
            feature_data = ONLINE_FEATURES[feature]
            embed = discord.Embed(
                title=feature_data['title'],
                description=feature_data['content'],
                color=discord.Color.blue()
            )
            
        await interaction.response.send_message(embed=embed) 