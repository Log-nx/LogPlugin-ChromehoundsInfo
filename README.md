# Chromehounds Information Plugin

A comprehensive information tool for the Chromehounds game, providing detailed information about lore, mechanics, parts, and strategies.

## Overview

The Chromehounds Information Plugin is designed to be a complete reference tool for players and fans of the Chromehounds game. It provides searchable access to game information including:

- **Lore & Background**: World setting, factions, and story elements
- **Game Mechanics**: Combat systems, construction mechanics, and multiplayer features
- **Parts & Equipment**: Detailed information about Hound components and weapons
- **Strategy & Tactics**: Combat strategies, build guides, and advanced tips

## Features

### 🔍 Smart Search System
- Keyword-based search across all game information
- Relevance scoring to show the most relevant results first
- Intelligent suggestions when no results are found
- Support for partial matches and synonyms

### 📚 Organized Categories
- **Lore**: Game world, factions, and background story
- **Mechanics**: How the game systems work
- **Parts**: Hound components and equipment details
- **Strategy**: Tactical advice and build strategies

### 🎨 Rich Discord Integration
- Beautiful embeds with category-specific colors
- Thumbnail images for visual appeal
- Proper formatting with Discord markdown
- Error handling with helpful messages

## Commands

### Main Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/chromehounds search <query>` | Search for any Chromehounds information | `/chromehounds search sniper` |
| `/chromehounds lore [topic]` | Get lore and background information | `/chromehounds lore factions` |
| `/chromehounds mechanics [topic]` | Get game mechanics information | `/chromehounds mechanics combat` |
| `/chromehounds parts [type]` | Get parts and equipment information | `/chromehounds parts weapons` |
| `/chromehounds strategy [topic]` | Get tactical and strategic information | `/chromehounds strategy builds` |
| `/chromehounds help` | Show help and usage information | `/chromehounds help` |

### Search Examples

- `/chromehounds search morskoj` - Information about the Morskoj Republic faction
- `/chromehounds search legs` - Information about different leg types
- `/chromehounds search sniper build` - Sniper build strategies and tips
- `/chromehounds search heat management` - Combat mechanics about heat systems

## Information Categories

### Lore & Background
- **Overview**: General game information and setting
- **World**: The fictional nation of Neroimus and its conflicts
- **Factions**: Detailed information about Morskoj, Sal Kar, and Tarakia

### Game Mechanics
- **Hound Construction**: Modular mech building system
- **Combat System**: Lock-on, damage, heat, and radar mechanics
- **Multiplayer**: Clan warfare and persistent world systems

### Parts & Equipment
- **Legs**: Bipedal, quadrupedal, tank treads, hover, and reverse-joint
- **Weapons**: Rifles, cannons, missiles, sniper rifles, shotguns, machine guns
- **Equipment**: Radar, cooling, armor, ammunition, and communication systems

### Strategy & Tactics
- **General Tactics**: Positioning, coordination, heat management
- **Build Strategies**: Sniper, assault, support, scout, and artillery builds
- **Advanced Tips**: Lock-on timing, damage prediction, energy management

## Technical Details

### Plugin Structure
```
plugins/Chromehounds/
├── __init__.py          # Plugin package initialization
├── chromehounds.py      # Main plugin class and commands
├── data.py             # Game information database
├── plugin.json         # Plugin metadata
└── README.md           # This documentation
```

### Dependencies
- `discord.py` - Discord bot framework
- `asyncio` - Asynchronous programming support
- Standard Python libraries (logging, typing)

### Database
The plugin uses a static data structure stored in `data.py` containing:
- Comprehensive game information organized by category
- Search functionality with relevance scoring
- Quick reference mappings for common terms

## Installation

1. Place the `Chromehounds` folder in your bot's `plugins/` directory
2. Ensure all dependencies are installed (they should be in your bot's requirements.txt)
3. Restart your bot or reload plugins
4. The plugin will automatically register its commands

## Usage Tips

### Effective Searching
- Use specific keywords for better results
- Try different variations of terms (e.g., "mech" vs "hound")
- Combine terms for more specific searches (e.g., "sniper build")
- Use faction names, part types, or weapon names as search terms

### Command Shortcuts
- Use category commands for browsing: `/chromehounds lore`, `/chromehounds parts`
- Add specific topics to narrow results: `/chromehounds mechanics combat`
- Use the help command to see all available options

### Best Practices
- Start with broad searches and narrow down as needed
- Check multiple categories if you're not finding what you need
- Use the suggestions provided when searches return no results

## Customization

### Adding New Information
To add new game information:

1. Edit `data.py` and add entries to the appropriate data dictionaries
2. Follow the existing format with `title` and `content` fields
3. Update the search keywords in `QUICK_REFERENCES` if needed
4. Test the new information with search commands

### Modifying Commands
The plugin uses Discord's slash command system. To modify commands:

1. Edit the command definitions in `chromehounds.py`
2. Update the help text and documentation accordingly
3. Test the changes in a development environment

## Support

For issues, suggestions, or contributions:
- Check the bot logs for error messages
- Ensure all dependencies are properly installed
- Verify the plugin structure matches the expected format
- Test commands in a development environment before deploying

## Version History

- **v1.0.0**: Initial release with comprehensive Chromehounds information database
  - Search functionality across all categories
  - Category-specific commands for browsing
  - Rich Discord embed formatting
  - Error handling and user feedback

## License

This plugin is part of the Logamus Bot project. Please refer to the main project license for usage terms. 