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

from plugins import Plugin
from .data import search_chromehounds_data, get_quick_suggestions, LORE_DATA, MECHANICS_DATA, PARTS_DATA, STRATEGY_DATA

class ChromehoundsInfo(Plugin):
    """Plugin for providing Chromehounds game information."""
    
    name = "chromehounds_info"
    description = "Comprehensive information tool for the Chromehounds game"
    version = "1.0.0"
    
    def __init__(self, bot):
        super().__init__(bot)
        self.max_results_per_search = 5
        self.max_content_length = 1800  # Discord embed description limit is 2048
    
    async def setup(self) -> bool:
        """Set up the plugin and register commands."""
        try:
            # Create a command group for Chromehounds
            self.chromehounds_group = app_commands.Group(
                name="chromehounds",
                description="Information and tools for the Chromehounds game"
            )
            
            # Add search command
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="search",
                    description="Search for Chromehounds information by keyword",
                    callback=self.search_command
                )
            )
            
            # Add category-specific commands
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="lore",
                    description="Get lore and background information about Chromehounds",
                    callback=self.lore_command
                )
            )
            
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="mechanics",
                    description="Get information about game mechanics",
                    callback=self.mechanics_command
                )
            )
            
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="parts",
                    description="Get information about Hound parts and equipment",
                    callback=self.parts_command
                )
            )
            
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="strategy",
                    description="Get tactical and strategic information",
                    callback=self.strategy_command
                )
            )
            
            # Add help command
            self.chromehounds_group.add_command(
                app_commands.Command(
                    name="help",
                    description="Get help with using the Chromehounds information system",
                    callback=self.help_command
                )
            )
            
            # Add the group to the bot's command tree
            self.bot.tree.add_command(self.chromehounds_group)
            
            self.logger.info("Chromehounds plugin commands registered successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error setting up Chromehounds plugin: {str(e)}")
            return False
    
    async def teardown(self) -> bool:
        """Clean up the plugin."""
        try:
            # Remove the command group from the bot's command tree
            self.bot.tree.remove_command("chromehounds")
            self.logger.info("Chromehounds plugin commands removed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error tearing down Chromehounds plugin: {str(e)}")
            return False
    
    def create_embed(self, title: str, content: str, category: str = None, color: int = 0x00ff00) -> discord.Embed:
        """Create a formatted embed for Chromehounds information."""
        # Truncate content if it's too long
        if len(content) > self.max_content_length:
            content = content[:self.max_content_length - 3] + "..."
        
        embed = discord.Embed(
            title=title,
            description=content,
            color=color
        )
        
        if category:
            embed.set_footer(text=f"Category: {category.title()}")
        
        # Set thumbnail based on category
        thumbnail_urls = {
            "lore": "https://via.placeholder.com/128x128/4a90e2/ffffff?text=LORE",
            "mechanics": "https://via.placeholder.com/128x128/f5a623/ffffff?text=MECH",
            "parts": "https://via.placeholder.com/128x128/7ed321/ffffff?text=PARTS",
            "strategy": "https://via.placeholder.com/128x128/d0021b/ffffff?text=STRAT"
        }
        
        if category and category in thumbnail_urls:
            embed.set_thumbnail(url=thumbnail_urls[category])
        
        return embed
    
    async def search_command(self, interaction: discord.Interaction, query: str) -> None:
        """Search for Chromehounds information by keyword."""
        await interaction.response.defer()
        
        try:
            if not query or len(query.strip()) < 2:
                embed = discord.Embed(
                    title="❌ Invalid Search",
                    description="Please provide a search term with at least 2 characters.",
                    color=0xff0000
                )
                await interaction.followup.send(embed=embed)
                return
            
            # Search for information
            results = search_chromehounds_data(query.strip())
            
            if not results:
                # Provide suggestions if no results found
                suggestions = get_quick_suggestions(query.strip())
                suggestion_text = "\n".join([f"• {s}" for s in suggestions]) if suggestions else "No suggestions available."
                
                embed = discord.Embed(
                    title="🔍 No Results Found",
                    description=f"No information found for '{query}'. Try these suggestions:\n\n{suggestion_text}",
                    color=0xffa500
                )
                await interaction.followup.send(embed=embed)
                return
            
            # Show top results
            embeds = []
            for i, result in enumerate(results[:self.max_results_per_search]):
                color_map = {
                    "lore": 0x4a90e2,
                    "mechanics": 0xf5a623,
                    "parts": 0x7ed321,
                    "strategy": 0xd0021b
                }
                
                color = color_map.get(result["category"], 0x00ff00)
                embed = self.create_embed(
                    title=f"🔍 {result['title']}",
                    content=result["content"],
                    category=result["category"],
                    color=color
                )
                
                if i == 0:
                    embed.set_author(name=f"Search Results for: {query}")
                
                embeds.append(embed)
            
            # Send the first embed immediately
            await interaction.followup.send(embed=embeds[0])
            
            # Send additional embeds if there are more results
            for embed in embeds[1:]:
                await asyncio.sleep(0.5)  # Small delay to avoid rate limits
                await interaction.followup.send(embed=embed)
            
            # Add a summary if there were more results
            if len(results) > self.max_results_per_search:
                summary_embed = discord.Embed(
                    title="📊 Search Summary",
                    description=f"Showing top {self.max_results_per_search} of {len(results)} results. Use more specific terms to narrow your search.",
                    color=0x808080
                )
                await interaction.followup.send(embed=summary_embed)
                
        except Exception as e:
            self.logger.error(f"Error in search command: {str(e)}")
            embed = discord.Embed(
                title="❌ Search Error",
                description="An error occurred while searching. Please try again.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed)
    
    async def lore_command(self, interaction: discord.Interaction, topic: str = None) -> None:
        """Get lore and background information about Chromehounds."""
        await interaction.response.defer()
        
        try:
            if topic:
                # Search for specific lore topic
                results = []
                for key, entry in LORE_DATA.items():
                    if topic.lower() in entry["title"].lower() or topic.lower() in entry["content"].lower():
                        results.append({
                            "key": key,
                            "title": entry["title"],
                            "content": entry["content"]
                        })
                
                if results:
                    embed = self.create_embed(
                        title=f"📚 {results[0]['title']}",
                        content=results[0]["content"],
                        category="lore",
                        color=0x4a90e2
                    )
                else:
                    embed = discord.Embed(
                        title="❌ Lore Topic Not Found",
                        description=f"No lore information found for '{topic}'. Try: overview, world, factions",
                        color=0xff0000
                    )
            else:
                # Show overview of available lore topics
                topics = "\n".join([f"• **{entry['title']}**" for entry in LORE_DATA.values()])
                embed = discord.Embed(
                    title="📚 Chromehounds Lore",
                    description=f"Available lore topics:\n\n{topics}\n\nUse `/chromehounds lore <topic>` for specific information.",
                    color=0x4a90e2
                )
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Error in lore command: {str(e)}")
            embed = discord.Embed(
                title="❌ Lore Error",
                description="An error occurred while retrieving lore information.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed)
    
    async def mechanics_command(self, interaction: discord.Interaction, topic: str = None) -> None:
        """Get information about game mechanics."""
        await interaction.response.defer()
        
        try:
            if topic:
                # Search for specific mechanics topic
                results = []
                for key, entry in MECHANICS_DATA.items():
                    if topic.lower() in entry["title"].lower() or topic.lower() in entry["content"].lower():
                        results.append({
                            "key": key,
                            "title": entry["title"],
                            "content": entry["content"]
                        })
                
                if results:
                    embed = self.create_embed(
                        title=f"⚙️ {results[0]['title']}",
                        content=results[0]["content"],
                        category="mechanics",
                        color=0xf5a623
                    )
                else:
                    embed = discord.Embed(
                        title="❌ Mechanics Topic Not Found",
                        description=f"No mechanics information found for '{topic}'. Try: construction, combat, multiplayer",
                        color=0xff0000
                    )
            else:
                # Show overview of available mechanics topics
                topics = "\n".join([f"• **{entry['title']}**" for entry in MECHANICS_DATA.values()])
                embed = discord.Embed(
                    title="⚙️ Chromehounds Mechanics",
                    description=f"Available mechanics topics:\n\n{topics}\n\nUse `/chromehounds mechanics <topic>` for specific information.",
                    color=0xf5a623
                )
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Error in mechanics command: {str(e)}")
            embed = discord.Embed(
                title="❌ Mechanics Error",
                description="An error occurred while retrieving mechanics information.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed)
    
    async def parts_command(self, interaction: discord.Interaction, part_type: str = None) -> None:
        """Get information about Hound parts and equipment."""
        await interaction.response.defer()
        
        try:
            if part_type:
                # Search for specific part type
                results = []
                for key, entry in PARTS_DATA.items():
                    if part_type.lower() in entry["title"].lower() or part_type.lower() in entry["content"].lower():
                        results.append({
                            "key": key,
                            "title": entry["title"],
                            "content": entry["content"]
                        })
                
                if results:
                    embed = self.create_embed(
                        title=f"🔧 {results[0]['title']}",
                        content=results[0]["content"],
                        category="parts",
                        color=0x7ed321
                    )
                else:
                    embed = discord.Embed(
                        title="❌ Part Type Not Found",
                        description=f"No parts information found for '{part_type}'. Try: legs, weapons, equipment",
                        color=0xff0000
                    )
            else:
                # Show overview of available part types
                topics = "\n".join([f"• **{entry['title']}**" for entry in PARTS_DATA.values()])
                embed = discord.Embed(
                    title="🔧 Chromehounds Parts",
                    description=f"Available part categories:\n\n{topics}\n\nUse `/chromehounds parts <type>` for specific information.",
                    color=0x7ed321
                )
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Error in parts command: {str(e)}")
            embed = discord.Embed(
                title="❌ Parts Error",
                description="An error occurred while retrieving parts information.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed)
    
    async def strategy_command(self, interaction: discord.Interaction, topic: str = None) -> None:
        """Get tactical and strategic information."""
        await interaction.response.defer()
        
        try:
            if topic:
                # Search for specific strategy topic
                results = []
                for key, entry in STRATEGY_DATA.items():
                    if topic.lower() in entry["title"].lower() or topic.lower() in entry["content"].lower():
                        results.append({
                            "key": key,
                            "title": entry["title"],
                            "content": entry["content"]
                        })
                
                if results:
                    embed = self.create_embed(
                        title=f"🎯 {results[0]['title']}",
                        content=results[0]["content"],
                        category="strategy",
                        color=0xd0021b
                    )
                else:
                    embed = discord.Embed(
                        title="❌ Strategy Topic Not Found",
                        description=f"No strategy information found for '{topic}'. Try: tactics, builds, tips",
                        color=0xff0000
                    )
            else:
                # Show overview of available strategy topics
                topics = "\n".join([f"• **{entry['title']}**" for entry in STRATEGY_DATA.values()])
                embed = discord.Embed(
                    title="🎯 Chromehounds Strategy",
                    description=f"Available strategy topics:\n\n{topics}\n\nUse `/chromehounds strategy <topic>` for specific information.",
                    color=0xd0021b
                )
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Error in strategy command: {str(e)}")
            embed = discord.Embed(
                title="❌ Strategy Error",
                description="An error occurred while retrieving strategy information.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed)
    
    async def help_command(self, interaction: discord.Interaction) -> None:
        """Get help with using the Chromehounds information system."""
        await interaction.response.defer()
        
        try:
            help_text = """
**Available Commands:**
• `/chromehounds search <query>` - Search for any Chromehounds information
• `/chromehounds lore [topic]` - Get lore and background information
• `/chromehounds mechanics [topic]` - Get game mechanics information
• `/chromehounds parts [type]` - Get parts and equipment information
• `/chromehounds strategy [topic]` - Get tactical and strategic information
• `/chromehounds help` - Show this help message

**Search Tips:**
• Use specific keywords like "sniper", "morskoj", "legs", "combat"
• Try category names: "lore", "mechanics", "parts", "strategy"
• Search for faction names: "morskoj", "sal kar", "tarakia"
• Look up weapon types: "rifle", "cannon", "missile"

**Examples:**
• `/chromehounds search sniper` - Find sniper-related information
• `/chromehounds lore factions` - Learn about the three factions
• `/chromehounds parts weapons` - See weapon system information
• `/chromehounds strategy builds` - Get Hound building strategies
            """
            
            embed = discord.Embed(
                title="🤖 Chromehounds Information System Help",
                description=help_text,
                color=0x00ff00
            )
            
            embed.set_footer(text="Chromehounds Information Plugin v1.0.0")
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            self.logger.error(f"Error in help command: {str(e)}")
            embed = discord.Embed(
                title="❌ Help Error",
                description="An error occurred while displaying help information.",
                color=0xff0000
            )
            await interaction.followup.send(embed=embed) 