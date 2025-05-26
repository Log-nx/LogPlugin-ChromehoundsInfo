"""
Chromehounds game data and information.
This module contains comprehensive information about the Chromehounds game.
"""

# Game Lore and Background
LORE_DATA = {
    "overview": {
        "title": "Chromehounds Overview",
        "content": """Chromehounds is a mech-based action game developed by FromSoftware and published by Sega in 2006 for Xbox 360. Set in a war-torn world where massive mechs called "Hounds" dominate the battlefield, players pilot customizable mechs in tactical combat scenarios.

The game features a unique modular mech construction system where players can build their own Hounds from various parts including legs, torsos, arms, weapons, and equipment. The game was known for its online multiplayer component and clan-based warfare system."""
    },
    "world": {
        "title": "The World of Chromehounds",
        "content": """The game is set in the fictional nation of Neroimus, a war-torn country caught between three major powers: Morskoj, Sal Kar, and Tarakia. Each faction has its own military doctrine, preferred mech configurations, and strategic objectives.

The conflict centers around control of Neroimus and its valuable resources, with each faction deploying their Hound units in large-scale battles across diverse terrain including urban areas, deserts, forests, and industrial complexes."""
    },
    "factions": {
        "title": "The Three Factions",
        "content": """**Morskoj Republic**: Known for their balanced approach to mech design and tactics. They favor versatile Hounds that can adapt to various combat situations.

**Sal Kar Federation**: Specialists in heavy assault mechs and defensive strategies. Their Hounds are typically heavily armored and equipped with powerful weapons.

**Tarakia Kingdom**: Masters of speed and reconnaissance. They prefer lightweight, fast-moving Hounds equipped with advanced sensors and mobility systems."""
    }
}

# Game Mechanics
MECHANICS_DATA = {
    "hound_construction": {
        "title": "Hound Construction System",
        "content": """Chromehounds features a modular construction system where players build their mechs from individual components:

**Core Components:**
- **Cockpit**: The pilot compartment and central control unit
- **Generator**: Powers all systems and determines energy capacity
- **Legs**: Determines mobility, stability, and weight capacity
- **Arms**: Mount weapons and equipment
- **Torso**: Houses the generator and provides mounting points

**Weight and Balance**: Each part has weight that affects performance. Heavier mechs move slower but can carry more equipment. Balance affects stability and turning speed."""
    },
    "combat_system": {
        "title": "Combat Mechanics",
        "content": """Combat in Chromehounds emphasizes tactical positioning and teamwork:

**Lock-on System**: Most weapons require target lock before firing. Lock-on time varies by weapon type and target distance.

**Damage System**: Hounds can lose individual parts when damaged. Losing legs affects mobility, losing arms removes weapons, and cockpit damage is critical.

**Heat Management**: Weapons generate heat when fired. Overheating can cause temporary weapon shutdown.

**Radar and Detection**: Various radar types provide different detection capabilities. Stealth systems can reduce detection range."""
    },
    "multiplayer": {
        "title": "Multiplayer and Clan System",
        "content": """The game featured extensive online multiplayer with a persistent war system:

**Clan Warfare**: Players could join one of the three factions and participate in large-scale territorial battles.

**Persistent World**: Battle outcomes affected the overall war map, with territories changing hands based on player actions.

**Squad System**: Players could form squads of up to 6 members for coordinated tactical operations.

**Rankings**: Individual and clan rankings tracked performance across various metrics."""
    }
}

# Parts and Equipment
PARTS_DATA = {
    "legs": {
        "title": "Leg Types and Characteristics",
        "content": """**Bipedal Legs**: Standard walking legs offering good balance of speed and stability. Best for general-purpose Hounds.

**Quadrupedal Legs**: Four-legged configuration providing excellent stability and weight capacity. Slower but very stable firing platform.

**Tank Treads**: Tracked locomotion offering high weight capacity and good stability. Vulnerable to leg damage but very durable.

**Hover Legs**: Advanced propulsion system allowing movement over any terrain. Fast but fragile and energy-intensive.

**Reverse-Joint Legs**: Digitigrade legs offering high speed and jumping ability. Less stable but excellent for hit-and-run tactics."""
    },
    "weapons": {
        "title": "Weapon Systems",
        "content": """**Rifles**: Balanced weapons with good range and accuracy. Standard choice for most combat situations.

**Machine Guns**: High rate of fire weapons effective against light armor. Good for suppression and close combat.

**Cannons**: Heavy weapons with high damage but slow rate of fire. Excellent against heavily armored targets.

**Missiles**: Guided weapons with various guidance systems. Can engage targets beyond visual range.

**Sniper Rifles**: Long-range precision weapons. Require steady aim but can eliminate targets at extreme distances.

**Shotguns**: Close-range weapons with spread damage. Devastating at short range but limited effectiveness at distance."""
    },
    "equipment": {
        "title": "Support Equipment",
        "content": """**Radar Systems**: Various types including search radar, target radar, and ECM systems. Essential for detection and targeting.

**Cooling Systems**: Manage heat buildup from weapons and movement. Critical for sustained combat operations.

**Armor Plating**: Additional protection at the cost of weight and mobility. Various types offer different protection levels.

**Ammunition Storage**: Extended ammunition capacity for prolonged engagements.

**Communication Equipment**: Enhanced squad coordination and information sharing capabilities."""
    }
}

# Strategies and Tips
STRATEGY_DATA = {
    "general_tactics": {
        "title": "General Combat Tactics",
        "content": """**Positioning**: Use terrain to your advantage. High ground provides better firing angles and detection range.

**Team Coordination**: Communicate with squad members. Coordinate attacks and share target information.

**Heat Management**: Monitor your heat levels. Overheating leaves you vulnerable and unable to fight effectively.

**Part Targeting**: Aim for specific parts. Destroying enemy weapons or legs can disable them without destroying the entire Hound.

**Radar Discipline**: Use passive sensors when possible. Active radar reveals your position to enemies."""
    },
    "build_strategies": {
        "title": "Hound Building Strategies",
        "content": """**Sniper Build**: Long-range legs, sniper rifle, advanced targeting systems. Stay at maximum range and eliminate key targets.

**Assault Build**: Heavy legs, multiple weapons, thick armor. Lead the charge and engage enemies directly.

**Support Build**: Balanced mobility, radar systems, communication equipment. Provide intelligence and coordinate team actions.

**Scout Build**: Fast legs, light weapons, stealth systems. Gather intelligence and harass enemy flanks.

**Artillery Build**: Stable platform, long-range missiles, targeting systems. Provide fire support from protected positions."""
    },
    "advanced_tips": {
        "title": "Advanced Combat Tips",
        "content": """**Lock-on Timing**: Learn weapon lock-on times. Pre-lock targets before engaging to reduce exposure time.

**Damage Prediction**: Understand damage models. Sometimes it's better to disable rather than destroy.

**Energy Management**: Balance generator capacity with equipment needs. Insufficient power reduces effectiveness.

**Terrain Usage**: Use buildings and obstacles for cover. Plan routes that minimize exposure to enemy fire.

**Squad Roles**: Assign specific roles to squad members. Specialization is more effective than generalization."""
    }
}

# Search function to find relevant information
def search_chromehounds_data(query: str) -> list:
    """
    Search through all Chromehounds data for relevant information.
    
    Args:
        query (str): Search term or phrase
        
    Returns:
        list: List of matching data entries with relevance scores
    """
    query_lower = query.lower()
    results = []
    
    # Search through all data categories
    all_data = {
        "lore": LORE_DATA,
        "mechanics": MECHANICS_DATA,
        "parts": PARTS_DATA,
        "strategy": STRATEGY_DATA
    }
    
    for category, data_dict in all_data.items():
        for key, entry in data_dict.items():
            title = entry["title"]
            content = entry["content"]
            
            # Calculate relevance score
            score = 0
            
            # Title matches are highly relevant
            if query_lower in title.lower():
                score += 10
            
            # Content matches are moderately relevant
            content_lower = content.lower()
            query_words = query_lower.split()
            
            for word in query_words:
                if word in content_lower:
                    score += content_lower.count(word)
            
            if score > 0:
                results.append({
                    "category": category,
                    "key": key,
                    "title": title,
                    "content": content,
                    "score": score
                })
    
    # Sort by relevance score (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)
    
    return results

# Quick reference data for common searches
QUICK_REFERENCES = {
    "factions": ["morskoj", "sal kar", "tarakia", "republic", "federation", "kingdom"],
    "parts": ["legs", "weapons", "arms", "torso", "cockpit", "generator", "radar"],
    "weapons": ["rifle", "cannon", "missile", "sniper", "shotgun", "machine gun"],
    "tactics": ["strategy", "combat", "positioning", "teamwork", "coordination"],
    "builds": ["sniper", "assault", "support", "scout", "artillery", "construction"]
}

def get_quick_suggestions(query: str) -> list:
    """
    Get quick suggestions based on the query.
    
    Args:
        query (str): Search query
        
    Returns:
        list: List of suggested search terms
    """
    query_lower = query.lower()
    suggestions = []
    
    for category, terms in QUICK_REFERENCES.items():
        for term in terms:
            if query_lower in term or term in query_lower:
                suggestions.append(f"{category}: {term}")
    
    return suggestions[:5]  # Return top 5 suggestions 