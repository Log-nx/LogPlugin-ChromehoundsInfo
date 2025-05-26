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
    version = "1.0.2"
    
    def __init__(self, bot):
        super().__init__(bot)
        self.logger = logging.getLogger("plugins.chromehounds_info")
        self._setup_commands()
        
    def _setup_commands(self):
        """Set up the plugin's commands."""
        
        # Main command group
        chromehounds_group = app_commands.Group(
            name="chromehounds",
            description="Chromehounds game information commands",
            guild_ids=None  # None means global commands
        )
        
        # Add commands to the group
        @chromehounds_group.command(name="search", description="Search for any Chromehounds information")
        @app_commands.describe(query="What would you like to know about Chromehounds?")
        async def search(interaction: discord.Interaction, query: str):
            await self._handle_search(interaction, query)
            
        @chromehounds_group.command(name="lore", description="Get lore and background information")
        @app_commands.describe(topic="The lore topic to learn about")
        async def lore(interaction: discord.Interaction, topic: Optional[str] = None):
            await self._handle_category(interaction, "lore", topic, [LORE_DATA, NATIONS_DATA, ORGANIZATIONS_DATA, HISTORICAL_DATA])
            
        @chromehounds_group.command(name="mechanics", description="Get game mechanics information")
        @app_commands.describe(topic="The mechanic topic to learn about")
        async def mechanics(interaction: discord.Interaction, topic: Optional[str] = None):
            await self._handle_category(interaction, "mechanics", topic, [MECHANICS_DATA, COMBAT_SYSTEMS, COMMUNICATION_DATA])
            
        @chromehounds_group.command(name="parts", description="Get parts and equipment information")
        @app_commands.describe(topic="The equipment topic to learn about")
        async def parts(interaction: discord.Interaction, topic: Optional[str] = None):
            await self._handle_category(interaction, "parts", topic, [EQUIPMENT_DATA, ROLE_TYPES])
            
        @chromehounds_group.command(name="strategy", description="Get tactical and strategic information")
        @app_commands.describe(topic="The strategy topic to learn about")
        async def strategy(interaction: discord.Interaction, topic: Optional[str] = None):
            await self._handle_category(interaction, "strategy", topic, [ROLE_TYPES, COMBAT_SYSTEMS])
        
        # Add the command group to the bot
        self.bot.tree.add_command(chromehounds_group)
        
    async def setup(self):
        """Set up the plugin."""
        try:
            self.logger.info("Setting up Chromehounds Information plugin...")
            import aiohttp
            self.logger.info("Chromehounds Information plugin setup complete!")
            return True
        except ImportError as e:
            self.logger.error(f"Required package not found: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Error during plugin setup: {str(e)}")
            return False
            
    async def _handle_search(self, interaction: discord.Interaction, query: str):
        """Handle the search command."""
        await interaction.response.defer()
        
        results = search_chromehounds_data(query)
        if not results:
            suggestions = get_quick_suggestions()
            embed = discord.Embed(
                title="No Results Found",
                description=f"No results found for '{query}'. Here are some suggested topics:",
                color=discord.Color.blue()
            )
            embed.add_field(
                name="Suggested Topics",
                value="\n".join(f"• {s}" for s in suggestions[:5]),
                inline=False
            )
        else:
            embed = discord.Embed(
                title=f"Search Results: {query}",
                color=discord.Color.blue()
            )
            for result in results:
                embed.add_field(
                    name=result["title"],
                    value=result["content"][:1024] if "content" in result else result["description"][:1024],
                    inline=False
                )
        
        await interaction.followup.send(embed=embed)
        
    async def _handle_category(self, interaction: discord.Interaction, category: str, topic: Optional[str], data_sources: List[dict]):
        """Handle category-specific commands."""
        await interaction.response.defer()
        
        if not topic:
            # Show category overview
            embed = discord.Embed(
                title=f"Chromehounds {category.title()} Information",
                description=f"Available topics in {category}:",
                color=discord.Color.blue()
            )
            
            # Collect all available topics from data sources
            topics = []
            for source in data_sources:
                for key, value in source.items():
                    if isinstance(value, dict) and "title" in value:
                        topics.append(value["title"])
                    else:
                        topics.append(key.replace("_", " ").title())
            
            # Sort and deduplicate topics
            topics = sorted(list(set(topics)))
            
            embed.add_field(
                name="Topics",
                value="\n".join(f"• {topic}" for topic in topics),
                inline=False
            )
            embed.add_field(
                name="Usage",
                value=f"Use `/chromehounds {category} <topic>` to get detailed information about a specific topic.",
                inline=False
            )
        else:
            # Search for specific topic
            results = []
            topic_lower = topic.lower()
            
            for source in data_sources:
                for key, value in source.items():
                    if isinstance(value, dict):
                        if ("title" in value and topic_lower in value["title"].lower()) or \
                           ("content" in value and topic_lower in value["content"].lower()) or \
                           ("description" in value and topic_lower in value["description"].lower()):
                            results.append(value)
            
            if not results:
                embed = discord.Embed(
                    title=f"No {category.title()} Results",
                    description=f"No results found for '{topic}' in {category}. Try using broader terms or check the category overview with `/chromehounds {category}`",
                    color=discord.Color.blue()
                )
            else:
                embed = discord.Embed(
                    title=f"{category.title()} Information: {topic}",
                    color=discord.Color.blue()
                )
                for result in results[:5]:  # Show top 5 results
                    embed.add_field(
                        name=result["title"],
                        value=result["content"][:1024] if "content" in result else result["description"][:1024],
                        inline=False
                    )
        
        await interaction.followup.send(embed=embed)

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