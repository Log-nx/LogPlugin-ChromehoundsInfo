"""
Chromehounds game data and information.
This module contains comprehensive information about the Chromehounds game.
"""

# Game Lore and Background
LORE_DATA = {
    "overview": {
        "title": "Chromehounds Overview",
        "content": """Chromehounds is a mech simulator video game developed by FromSoftware and published by Sega in 2006 for Xbox 360. Set in an alternate history timeline, the game features massive mechanized combat vehicles called HOUNDs battling for control of the Neroimus region near the Black Sea.

The game was directed by Takuji Yoshida, produced by Toshifumi Nabeshima, with art by Isao Saito and Hisao Yamada, and music composed by Kota Hoshino. It represented FromSoftware's vision of a realistic, team-based mech combat game with deep customization."""
    },
    "alternate_history": {
        "title": "Alternate History Timeline",
        "content": """The Chromehounds universe diverges from our timeline in 1945 with several key events:

• 1945: International arms manufacturer Rafzekael is founded after World War II
• 1980: Rafzekael unveils the first Advanced Combat Vehicle (ACV) based on stolen US bipedal tank designs
• 1981: Massive solar flares cause global infrastructure disruption, leading to geopolitical upheaval
• 1981-1982: Rafzekael distributes ACV technology to major world powers
• 1990s: Soviet Union splits into western GSSR (communist) and eastern Republic of Russia (democratic)
• 1992: Three new nations emerge in Neroimus region:
  - Democratic Republic of Tarakia (US-backed democracy)
  - Republic of Morskoj (former Soviet state)
  - Kingdom of Sal Kar (mineral-rich monarchy)"""
    },
    "world": {
        "title": "The World of Chromehounds",
        "content": """The game takes place in an alternate 2006 where conventional air power has been largely replaced by massive ground-based mechanized units called HOUNDs. The Neroimus region, located on the southeast coast of the Black Sea, has become a flashpoint of tension between three nations with conflicting ideologies and shared borders.

The region is characterized by diverse terrain including urban areas, deserts, forests, and industrial complexes. The infrastructure is dominated by COMBAS communication towers, which are crucial for military operations and coordination between HOUND units."""
    },
    "factions": {
        "title": "The Three Nations",
        "content": """**Democratic Republic of Tarakia**
• A multi-ethnic democracy with economic backing from the United States
• Emphasizes balanced military doctrine and adaptable tactics
• Fields versatile HOUNDs suitable for various combat roles
• Promotes technological advancement and strategic flexibility

**Republic of Morskoj**
• Former Soviet state dealing with communist insurgency supported by GSSR
• Specializes in heavy assault and defensive warfare
• Deploys heavily armored HOUNDs with overwhelming firepower
• Values strength and durability in military equipment

**Kingdom of Sal Kar**
• Mineral-rich monarchy formed from a breakaway region
• Masters of mobility and reconnaissance warfare
• Operates fast, agile HOUNDs with advanced sensors
• Focuses on hit-and-run tactics and superior battlefield awareness"""
    },
    "rafzekael": {
        "title": "Rafzekael Corporation",
        "content": """Rafzekael is a powerful international arms manufacturer founded in 1945. Key achievements include:

• Development of the first Advanced Combat Vehicle (ACV)
• Creation of the standardized hexagonal weapon mounting system
• Operation of an elite mercenary division
• Leading role in HOUND technology advancement

The corporation maintains a reputation for having the best mercenary HOUND pilots in the world, though their true motives remain mysterious."""
    },
    "cerberus": {
        "title": "Cerberus Squad",
        "content": """A legendary three-man HOUND unit known for their powerful weapons and ruthless tactics. Led by Edgardo Gilardino, they play a crucial role in triggering the Neroimus War through their attack on the Sal Kari base in the Tagin region.

Their actions are revealed to be part of a larger conspiracy, though their ultimate employer's identity remains unknown. Their legacy lives on in the advanced combat techniques they developed."""
    }
}

# Game Development and History
DEVELOPMENT_DATA = {
    "overview": {
        "title": "Development History",
        "content": """Chromehounds was developed by FromSoftware and published by Sega in 2006 for the Xbox 360. The game was directed by Takuji Yoshida, produced by Toshifumi Nabeshima, with art by Isao Saito and Hisao Yamada, and music composed by Kota Hoshino.

The game was first revealed at Tokyo Game Show 2003 under the name "CHROME HOUND -AGE OF ARMS-". It represented FromSoftware's vision of a realistic, team-based mech combat game with deep customization options, building on their experience from the Armored Core series."""
    },
    "setting": {
        "title": "Game Setting",
        "content": """Set in an alternate history timeline, Chromehounds takes place in the Neroimus region near the Black Sea, where three nations - Sal Kar, Tarakia, and Morskoj - are locked in a violent struggle for control. The conflict, known as the Neroimus War, is fought primarily using massive mechanized combat vehicles called HOUNDs.

Players take on the role of mercenaries in the Rafzakael unit, which can be hired by any of the three nations. The single-player campaign is set in the period leading up to the full outbreak of war, dealing with various terrorist threats and border conflicts."""
    }
}

# Role Types (RT)
ROLE_TYPES = {
    "soldier": {
        "title": "Soldier",
        "description": """Front-line combat specialist:
- Balanced mix of firepower and mobility
- Effective at short to medium range combat
- Typically uses bipedal legs with Medium Cockpit
- Primary weapons include assault rifles, rocket launchers, grenades
- Versatile role suitable for various combat situations""",
        "equipment": {
            "recommended": [
                "Medium Cockpit",
                "Bipedal Legs",
                "Assault Rifles",
                "Rocket Launchers",
                "Grenade Launchers",
                "Shotguns"
            ],
            "tactics": [
                "Front-line assault",
                "Objective capture",
                "Squad support",
                "Base defense",
                "COMBAS tower capture"
            ]
        }
    },
    "sniper": {
        "title": "Sniper",
        "description": """Long-range precision specialist:
- Focuses on long-distance engagement
- Uses reverse-jointed or multiped legs
- Light/Medium Cockpit for better accuracy
- Specializes in anti-HOUND operations
- Requires precise aim and leading targets""",
        "equipment": {
            "recommended": [
                "Light/Medium Cockpit",
                "Reverse-jointed Legs",
                "Multiped Base",
                "Sniper Rifles",
                "Anti-HOUND Cannons",
                "Precision Targeting Systems"
            ],
            "tactics": [
                "Long-range support",
                "Target elimination",
                "Area denial",
                "Cover fire",
                "Anti-HOUND operations"
            ]
        }
    },
    "defender": {
        "title": "Defender",
        "description": """Heavy defense specialist:
- Heavily armored weapon platform
- Uses caterpillar tracks for mobility
- Heavy/Super Heavy Cockpit
- Focuses on area control and defense
- Excellent at holding strategic points""",
        "equipment": {
            "recommended": [
                "Heavy/Super Heavy Cockpit",
                "Caterpillar Tracks",
                "Anti-HOUND Cannons",
                "Shotguns",
                "Missile Launchers",
                "Heavy Armor Plating"
            ],
            "tactics": [
                "Base defense",
                "Area control",
                "Choke point defense",
                "Squad protection",
                "Resource point defense"
            ]
        }
    },
    "scout": {
        "title": "Scout",
        "description": """Reconnaissance and mobility specialist:
- Fastest and lightest HOUND type
- Uses hover or wheel-based movement
- Light Cockpit for maximum speed
- Critical for early game information
- Essential for COMBAS tower capture""",
        "equipment": {
            "recommended": [
                "Light Cockpit",
                "Hover System",
                "Wheeled Base",
                "Light Weapons",
                "Anti-HOUND Piles",
                "Speed Enhancement Chips"
            ],
            "tactics": [
                "COMBAS capture",
                "Reconnaissance",
                "Hit-and-run attacks",
                "Early warning",
                "Resource point capture"
            ]
        }
    },
    "heavy_gunner": {
        "title": "Heavy Gunner",
        "description": """Artillery and support specialist:
- Specializes in indirect fire support
- Uses multiped legs for stability
- Light/Medium Cockpit with heavy weapons
- Requires coordination with spotters
- Master of area denial tactics""",
        "equipment": {
            "recommended": [
                "Light/Medium Cockpit",
                "Multiped Legs",
                "Howitzers",
                "Artillery Cannons",
                "Missile Systems",
                "Stabilization Systems"
            ],
            "tactics": [
                "Artillery support",
                "Area denial",
                "Base bombardment",
                "Support fire",
                "Strategic bombardment"
            ]
        }
    },
    "commander": {
        "title": "Tactics Commander",
        "description": """Strategic command and control specialist:
- Provides battlefield communication and intel
- Uses NA maker for extended communications
- Light/Heavy Cockpit with defensive weapons
- Critical for squad coordination
- Last line of defense""",
        "equipment": {
            "recommended": [
                "Light/Heavy Cockpit",
                "Caterpillar Tracks",
                "NA Maker",
                "Machine Guns",
                "Shotguns",
                "Mortars"
            ],
            "tactics": [
                "Squad coordination",
                "Battle management",
                "Communication control",
                "Strategic planning",
                "Intelligence gathering"
            ]
        }
    }
}

# Equipment and Customization
EQUIPMENT_DATA = {
    "chassis": {
        "title": "Chassis Types",
        "description": """The base frame that determines a HOUND's mobility:
- Bipedal: Standard humanoid legs with forward knee joints
- Reverse-jointed: Bird-like legs with backward knee joints
- Multiped: Multiple legs for heavy weapon stability
- Caterpillar: Tank treads for heavy armor support
- Hover: Air cushion system for water crossing
- Wheeled: High speed on flat terrain""",
        "types": {
            "bipedal": {
                "strengths": [
                    "Balanced mobility and stability",
                    "Good for general combat",
                    "Effective weapon platform",
                    "Decent turning radius",
                    "Moderate weight capacity"
                ],
                "best_for": ["Soldier", "Commander"]
            },
            "reverse_jointed": {
                "strengths": [
                    "Enhanced stability for sniping",
                    "Good balance at rest",
                    "Precise movement control",
                    "Moderate speed",
                    "Excellent for precision weapons"
                ],
                "best_for": ["Sniper", "Heavy Gunner"]
            },
            "multiped": {
                "strengths": [
                    "Maximum stability",
                    "Highest weight capacity",
                    "Excellent for heavy weapons",
                    "Good on rough terrain",
                    "Strong defensive platform"
                ],
                "best_for": ["Heavy Gunner", "Defender"]
            },
            "caterpillar": {
                "strengths": [
                    "Heavy armor capacity",
                    "Stable weapon platform",
                    "Good for defensive roles",
                    "Reliable on most terrain",
                    "High pushing power"
                ],
                "best_for": ["Defender", "Commander"]
            },
            "hover": {
                "strengths": [
                    "Water traversal",
                    "High speed",
                    "Good for scouting",
                    "Excellent mobility",
                    "Quick direction changes"
                ],
                "best_for": ["Scout"]
            },
            "wheeled": {
                "strengths": [
                    "Fastest on flat ground",
                    "Good for quick strikes",
                    "Excellent for scouting",
                    "Fast acceleration",
                    "Low profile"
                ],
                "best_for": ["Scout"]
            }
        }
    },
    "cockpits": {
        "title": "Cockpit Types",
        "description": """The core component that houses weapons and systems:
- Light: Maximum speed and agility
- Medium: Balanced performance
- Heavy: Maximum armor and stability
- Super Heavy: Ultimate protection""",
        "types": {
            "light": {
                "features": [
                    "High mobility",
                    "Quick turning",
                    "Low weight",
                    "Good for scouts",
                    "Limited armor"
                ]
            },
            "medium": {
                "features": [
                    "Balanced protection",
                    "Good weapon capacity",
                    "Moderate speed",
                    "Versatile mounting",
                    "Standard stability"
                ]
            },
            "heavy": {
                "features": [
                    "High protection",
                    "Large weapon capacity",
                    "Slow movement",
                    "Good stability",
                    "Heavy weight"
                ]
            },
            "super_heavy": {
                "features": [
                    "Maximum protection",
                    "Highest weapon capacity",
                    "Very slow movement",
                    "Excellent stability",
                    "Extreme weight"
                ]
            }
        }
    },
    "weapons": {
        "title": "Weapon Systems",
        "description": """Various weapon types for different combat roles:
- Light Arms: Machine guns, rifles, shotguns
- Heavy Arms: Cannons, missile launchers
- Special Weapons: HEAT launchers, pile bunkers
- Support Systems: Smoke generators, ECM""",
        "categories": {
            "light_arms": {
                "types": [
                    "Machine Guns",
                    "Assault Rifles",
                    "Sniper Rifles",
                    "Shotguns",
                    "Grenade Launchers"
                ],
                "characteristics": [
                    "High rate of fire",
                    "Good ammunition capacity",
                    "Moderate damage",
                    "Various ranges",
                    "Light weight"
                ]
            },
            "heavy_arms": {
                "types": [
                    "Anti-HOUND Cannons",
                    "Howitzers",
                    "Missile Launchers",
                    "Artillery Pieces",
                    "Heavy Mortars"
                ],
                "characteristics": [
                    "High damage",
                    "Limited ammunition",
                    "Heavy weight",
                    "Long range",
                    "Area effect damage"
                ]
            },
            "special_weapons": {
                "types": [
                    "HEAT Launchers",
                    "Pile Bunkers",
                    "Mine Launchers",
                    "Anti-HOUND Piles",
                    "Bomb Launchers"
                ],
                "characteristics": [
                    "Specialized damage",
                    "Unique effects",
                    "Tactical applications",
                    "Situational use",
                    "Special ammunition"
                ]
            }
        }
    },
    "generators": {
        "title": "Generator Systems",
        "description": """Power plants that determine operational capability:
- Small: Light weight but limited power
- Medium: Balanced performance
- Large: Maximum power but heavy
- Special: Unique characteristics""",
        "types": {
            "small": {
                "features": [
                    "Light weight",
                    "Quick startup",
                    "Limited power output",
                    "Good for scouts",
                    "Efficient fuel use"
                ]
            },
            "medium": {
                "features": [
                    "Balanced weight",
                    "Good power output",
                    "Standard fuel capacity",
                    "Versatile application",
                    "Reliable performance"
                ]
            },
            "large": {
                "features": [
                    "Maximum power",
                    "Heavy weight",
                    "High fuel capacity",
                    "Good for heavy weapons",
                    "Slow startup"
                ]
            }
        }
    },
    "assist_parts": {
        "title": "Support Systems",
        "description": """Additional equipment for enhanced capabilities:
- Sensors: Night vision, thermal imaging
- Defense: ECM, missile counters
- Support: NA maker, fuel tanks
- Armor: Additional protection""",
        "categories": {
            "sensors": [
                "Night Vision",
                "Thermal Imaging",
                "Range Finder",
                "Target Tracker",
                "Mine Detector"
            ],
            "defense": [
                "ECM System",
                "Missile Counter",
                "Smoke Generator",
                "Chaff Dispenser",
                "Active Defense"
            ],
            "support": [
                "NA Maker",
                "Fuel Tanks",
                "Repair System",
                "Ammo Resupply",
                "Boost Enhancer"
            ],
            "armor": [
                "Frontal Armor",
                "Side Skirts",
                "Reactive Armor",
                "Composite Plates",
                "Shield Generator"
            ]
        }
    }
}

# Combat Systems
COMBAT_SYSTEMS = {
    "damage_types": {
        "title": "Damage Systems",
        "description": """Two primary damage types affect combat:
- Kinetic: Physical impact damage
- Chemical: Explosive and energy damage
- Defense values affect damage calculation
- Critical hits can disable systems
- Component damage affects performance""",
        "mechanics": [
            "Damage reduction by armor",
            "Critical hit locations",
            "System failures",
            "Progressive degradation",
            "Repair limitations"
        ]
    },
    "combat_ranges": {
        "title": "Combat Ranges",
        "description": """Effective weapon ranges affect tactics:
- Close: 0-200m (Shotguns, HEAT)
- Medium: 200-500m (Rifles, Cannons)
- Long: 500-1000m (Snipers)
- Extreme: 1000m+ (Artillery)""",
        "factors": [
            "Weapon accuracy at range",
            "Damage falloff",
            "Environmental effects",
            "Target movement",
            "Terrain impact"
        ]
    },
    "targeting": {
        "title": "Targeting Systems",
        "description": """Advanced targeting mechanics:
- Manual aim mode
- Assisted targeting
- Range compensation
- Lead indicators
- Lock-on systems""",
        "features": [
            "Accuracy modifiers",
            "Range calculation",
            "Target tracking",
            "Weapon spread",
            "Environmental factors"
        ]
    },
    "communication": {
        "title": "Communication Systems",
        "description": """COMBAS network features:
- Squad coordination
- Target marking
- Area control
- Strategic planning
- Intelligence sharing""",
        "elements": [
            "NA maker coverage",
            "Squad commands",
            "Map control",
            "Target designation",
            "Status reporting"
        ]
    }
}

# Game Mechanics
MECHANICS_DATA = {
    "combat": {
        "title": "Combat Mechanics",
        "content": """Core combat systems in Chromehounds:
- Damage calculation based on weapon type and armor
- Critical hit system for component damage
- Heat management during sustained fire
- Ammunition and reload mechanics
- Line of sight and targeting systems
- Weather and visibility effects""",
        "features": [
            "Realistic ballistics",
            "Component damage",
            "Heat management",
            "Ammo management",
            "Environmental factors"
        ]
    },
    "customization": {
        "title": "HOUND Customization",
        "content": """Comprehensive customization system:
- Modular component assembly
- Weight and balance management
- Power distribution systems
- Performance optimization
- Visual customization options""",
        "features": [
            "Part compatibility",
            "Weight limits",
            "Power requirements",
            "Heat efficiency",
            "Aesthetic options"
        ]
    },
    "damage": {
        "title": "Damage System",
        "content": """Complex damage calculation system:
- Kinetic and chemical damage types
- Armor penetration mechanics
- Component-specific damage
- Critical hit locations
- Progressive system damage""",
        "features": [
            "Multiple damage types",
            "Location-based damage",
            "System degradation",
            "Repair mechanics",
            "Protection systems"
        ]
    }
}

# Nations and Factions
NATIONS_DATA = {
    "tarakia": {
        "title": "Democratic Republic of Tarakia",
        "description": """Western nation in the Neroimus region:
- Formed in June 1992 along the Black Sea coast
- Backed financially by the United States
- Largest territory and population of the three nations
- Democratic multi-ethnic republic
- Balanced and versatile military equipment""",
        "details": {
            "size": "68,540 sq. km",
            "population": "4,520,000+",
            "capital": "Xeres",
            "government": "Republic (4-year presidential term)",
            "language": "English",
            "religion": "Multi-denominational",
            "currency": "Tarakian Dollar",
            "industries": [
                "Farming",
                "Iron and Steel",
                "Machinery",
                "Military Equipment"
            ]
        },
        "military": {
            "equipment": {
                "characteristics": [
                    "Balanced performance",
                    "Wide variety of parts",
                    "Medium-weight focus",
                    "Good quality-to-cost ratio",
                    "Standardized designs"
                ],
                "strengths": [
                    "Versatile weapon systems",
                    "Good parts compatibility",
                    "Reliable performance",
                    "Cost-effective equipment",
                    "Advanced technology"
                ]
            }
        }
    },
    "morskoj": {
        "title": "Republic of Morskoj",
        "description": """Eastern nation in the Neroimus region:
- Gained independence from Soviet Union in 1996
- Continues to face pressure from Great Soviet Socialist Republic
- Strong industrial and military tradition
- Focuses on heavy, durable equipment
- Significant natural resources""",
        "details": {
            "size": "62,380 sq. km",
            "population": "3,580,000+",
            "capital": "Ostrov",
            "government": "Republic (4-year presidential term)",
            "language": "Morskovian, Russian",
            "religion": "Russian Orthodox, others",
            "currency": "Isra",
            "industries": [
                "Farming",
                "Metallurgy",
                "Mining",
                "Timber",
                "Heavy Industry"
            ]
        },
        "military": {
            "equipment": {
                "characteristics": [
                    "Heavy armor focus",
                    "Durable construction",
                    "High firepower",
                    "Robust systems",
                    "Industrial efficiency"
                ],
                "strengths": [
                    "Superior armor protection",
                    "Heavy weapons capability",
                    "Long service life",
                    "Reliable in harsh conditions",
                    "Powerful engines"
                ]
            }
        }
    },
    "sal_kar": {
        "title": "Kingdom of Sal Kar",
        "description": """Southern nation in the Neroimus region:
- Reformed in 1989 under King Sal Kar XIV
- Backed by Far East Union
- Rich in natural resources including gas
- Smallest but resource-rich territory
- Specializes in light, mobile equipment""",
        "details": {
            "size": "20,800 sq. km",
            "population": "2,280,000+",
            "capital": "Qura",
            "government": "Limited Monarchy",
            "language": "Karic",
            "religion": "Sal Kari State Religion",
            "currency": "Ziyad",
            "industries": [
                "Natural Gas",
                "Oil",
                "Mining",
                "Light Industry",
                "Resource Processing"
            ]
        },
        "military": {
            "equipment": {
                "characteristics": [
                    "Light weight designs",
                    "High mobility focus",
                    "Advanced electronics",
                    "Desert warfare specialty",
                    "Resource efficiency"
                ],
                "strengths": [
                    "Speed and agility",
                    "Advanced targeting systems",
                    "Heat management",
                    "Terrain adaptation",
                    "Fuel efficiency"
                ]
            }
        }
    }
}

# Organizations
ORGANIZATIONS_DATA = {
    "rafzakael": {
        "title": "Rafzakael Corporation",
        "description": """International arms manufacturer and mercenary organization:
- Founded in 1945 after World War II
- Developed first Advanced Combat Vehicle (ACV) in 1980
- Pioneer of HOUND technology
- Premier mercenary force provider
- Global military equipment supplier""",
        "history": {
            "key_events": [
                "1945: Founded after WWII",
                "1980: First ACV unveiled",
                "1981: Global ACV distribution",
                "1990s: HOUND development",
                "2000s: Neroimus deployment"
            ],
            "achievements": [
                "ACV technology pioneer",
                "HOUND development leader",
                "Elite mercenary force",
                "Global arms supplier",
                "Military innovation"
            ]
        }
    },
    "cerberus": {
        "title": "Cerberus Squad",
        "description": """Elite and mysterious HOUND unit:
- Legendary three-man squad
- Known for ruthless tactics
- Advanced prototype equipment
- Secretive operations
- Strategic influence""",
        "characteristics": {
            "combat": [
                "Superior tactics",
                "Advanced equipment",
                "Ruthless efficiency",
                "Strategic operations",
                "Elite pilots"
            ],
            "influence": [
                "Political manipulation",
                "Military intervention",
                "Strategic destabilization",
                "Technological superiority",
                "Psychological impact"
            ]
        }
    }
}

# Historical Events
HISTORICAL_DATA = {
    "timeline": {
        "title": "Chromehounds Timeline",
        "description": """Key events in the Chromehounds universe:
1945: Rafzakael founded after WWII
1980: First ACV developed
1981: Global solar flare crisis
1989: Sal Kar reformed
1992: Tarakia established
1996: Morskoj gains independence
1997: Sal Kar gas fields discovered
2000s: Neroimus conflict begins""",
        "events": {
            "pre_war": [
                "1945: Rafzakael foundation",
                "1980: ACV development",
                "1981: Solar flare crisis",
                "1980s: HOUND development",
                "1990s: Nation formation"
            ],
            "war_period": [
                "2000: Mercenary deployment",
                "2003: Border tensions",
                "2006: Sal Kar base attack",
                "2006: War declaration",
                "2006: Neroimus War begins"
            ]
        }
    },
    "background": {
        "title": "Historical Background",
        "description": """Major historical developments:
- Post-WWII military industrial growth
- Cold War technological advancement
- Solar flare crisis and global upheaval
- Nation-state reformation period
- Rise of mercenary forces""",
        "factors": {
            "technological": [
                "ACV development",
                "HOUND evolution",
                "Weapons advancement",
                "Communication systems",
                "Military innovation"
            ],
            "political": [
                "Nation formation",
                "Alliance systems",
                "Resource conflicts",
                "Military doctrine",
                "Strategic interests"
            ]
        }
    }
}

# Communication Systems
COMMUNICATION_DATA = {
    "combas": {
        "title": "COMBAS System",
        "content": """Communication Base System (COMBAS) is the backbone of battlefield communications:
- Tower structures placed throughout battlefields
- Creates Network Areas (NA) for team communication
- Must be captured to establish communication links
- Essential for coordinating team movements
- Visible indicators show controlling faction
- Range varies based on tower type and terrain""",
        "tactical_use": [
            "Establish communication networks",
            "Create safe zones for team coordination",
            "Strategic points for territory control",
            "Enable commander tactical oversight",
            "Support long-range operations"
        ]
    },
    "network_areas": {
        "title": "Network Areas (NA)",
        "content": """Zones of active communication created by COMBAS towers and NA makers:
- Allow real-time communication between squad members
- Display friendly and enemy positions on tactical map
- Essential for coordinated attacks and defense
- Can be expanded or linked with multiple towers
- Affected by terrain and interference""",
        "features": [
            "Real-time tactical updates",
            "Position tracking of allied forces",
            "Command and control capabilities",
            "Strategic planning support",
            "Battlefield awareness enhancement"
        ]
    },
    "commander_systems": {
        "title": "Commander Communication Systems",
        "content": """Specialized equipment used by Tactics Commanders:
- NA makers create mobile communication zones
- Advanced radar and detection capabilities
- Command and control interface systems
- Strategic planning and coordination tools
- Real-time battlefield management""",
        "capabilities": [
            "Mobile command centers",
            "Advanced enemy detection",
            "Squad coordination tools",
            "Strategic overlay systems",
            "Battlefield management interface"
        ]
    }
}

# Online Features
ONLINE_FEATURES = {
    "neroimus_war": {
        "title": "The Neroimus War",
        "content": """Persistent online campaign mode where three nations battle for control:
- Dynamic territory control system
- Squad-based warfare mechanics
- Resource and strategic management
- Nation-specific missions and objectives
- Real-time territory updates""",
        "features": [
            "Persistent world warfare",
            "Strategic territory control",
            "Nation-based objectives",
            "Squad warfare mechanics",
            "Resource management"
        ]
    },
    "squad_mechanics": {
        "title": "Squad System",
        "content": """Team-based organization and combat system:
- Create or join squads (clans)
- Coordinate with squad members
- Share resources and intelligence
- Participate in squad missions
- Contribute to nation's war effort""",
        "features": [
            "Squad formation and management",
            "Team coordination tools",
            "Resource sharing systems",
            "Squad-specific missions",
            "Contribution tracking"
        ]
    },
    "territory_control": {
        "title": "Territory Control System",
        "content": """Dynamic system for controlling the Neroimus region:
- Capture and hold strategic points
- Manage resource distribution
- Defend territory from enemies
- Coordinate large-scale operations
- Influence war progression""",
        "mechanics": [
            "Strategic point capture",
            "Resource management",
            "Defense operations",
            "Large-scale coordination",
            "War influence systems"
        ]
    }
}

# Technical Details
TECHNICAL_DATA = {
    "graphics": {
        "title": "Graphics and Presentation",
        "content": """Chromehounds featured:
- Detailed mech models with visible battle damage
- Dynamic weather effects
- Day/night cycles with working vision modes
- Destructible environments and structures
- Realistic physics-based movement
- High-quality explosion effects
- Footprint tracking in various terrain types"""
    },
    
    "audio": {
        "title": "Audio Design",
        "content": """The game's audio featured:
- Symphonic soundtrack
- Realistic mechanical sound effects
- Position-based audio for combat
- Voice communication integration
- Environmental audio effects
- Impact and explosion sound design"""
    }
}

# Legacy and Impact
LEGACY_DATA = {
    "influence": {
        "title": "Game Legacy",
        "content": """Chromehounds was notable for:
- Being one of the first persistent online warfare games on consoles
- Pioneering team-based mech combat with specialized roles
- Introducing innovative communication mechanics
- Setting new standards for mech customization
- Inspiring future mech combat games
- Creating a dedicated community that remains active
- Influencing FromSoftware's approach to online gaming"""
    },
    
    "community": {
        "title": "Community Impact",
        "content": """The game's community was known for:
- Forming lasting squadrons (clans)
- Developing complex tactical strategies
- Creating specialized team compositions
- Maintaining active forums and discussion boards
- Organizing tournaments and events
- Continuing to seek ways to revive the game
- Supporting spiritual successors like M.A.V. (Modular Assault Vehicle)"""
    }
}

# Search function to find relevant information
def search_chromehounds_data(query: str) -> list:
    """
    Search through the Chromehounds data based on keywords.
    Returns relevant information matching the search query.
    
    Args:
        query (str): Search query string
        
    Returns:
        list: List of dictionaries containing matching information
    """
    query = query.lower()
    results = []
    
    # Define searchable data structures
    search_spaces = {
        "lore": LORE_DATA,
        "roles": ROLE_TYPES,
        "equipment": EQUIPMENT_DATA,
        "combat": COMBAT_SYSTEMS,
        "nations": NATIONS_DATA,
        "organizations": ORGANIZATIONS_DATA,
        "history": HISTORICAL_DATA,
        "communication": COMMUNICATION_DATA,
        "online": ONLINE_FEATURES,
        "technical": TECHNICAL_DATA,
        "legacy": LEGACY_DATA,
        "mechanics": MECHANICS_DATA
    }
    
    # Search through each data structure
    for category, data in search_spaces.items():
        # Search through top-level entries
        for key, value in data.items():
            if isinstance(value, dict):
                # Check if query matches in title or content
                if 'title' in value and query in value['title'].lower():
                    results.append(value)
                elif 'content' in value and query in value['content'].lower():
                    results.append(value)
                elif 'description' in value and query in value['description'].lower():
                    results.append(value)
                
                # Search through nested dictionaries
                for subkey, subvalue in value.items():
                    if isinstance(subvalue, (list, str)):
                        # Convert to string for searching
                        content = str(subvalue).lower()
                        if query in content and value not in results:
                            results.append(value)
    
    # If no exact matches found, try matching keywords
    if not results:
        for keywords in QUICK_REFERENCES.values():
            if any(keyword.lower() in query for keyword in keywords):
                # Add relevant top-level entries
                for category, data in search_spaces.items():
                    for key, value in data.items():
                        if isinstance(value, dict) and 'title' in value:
                            results.append(value)
                break
    
    return results[:5]  # Return top 5 most relevant results

# Quick reference data for common searches
QUICK_REFERENCES = {
    "factions": ["morskoj", "sal kar", "tarakia", "republic", "federation", "kingdom"],
    "parts": ["legs", "weapons", "arms", "torso", "cockpit", "generator", "radar"],
    "weapons": ["rifle", "cannon", "missile", "sniper", "shotgun", "machine gun", "howitzer", "mortar"],
    "tactics": ["strategy", "combat", "positioning", "teamwork", "coordination"],
    "builds": ["sniper", "assault", "support", "scout", "artillery", "construction"],
    "history": ["rafzekael", "cerberus", "neroimus", "alternate history", "timeline"],
    "mechanics": ["construction", "combat", "damage", "communication", "role types"]
}

def get_quick_suggestions() -> list:
    """
    Returns a list of common search terms and topics about Chromehounds.
    """
    return [
        "HOUND types and roles",
        "Weapons and equipment",
        "Game mechanics",
        "Online features",
        "Nation backgrounds",
        "Combat tactics",
        "Customization options",
        "COMBAS system",
        "Communication features",
        "Territory control",
        "Weapon types",
        "Combat ranges",
        "Damage system",
        "Targeting mechanics",
        "Nation equipment",
        "Manufacturers",
        "Communication systems",
        "Squad mechanics",
        "Role types",
        "Movement systems",
        "Equipment types",
        "Generator systems",
        "Support features",
        "Combat roles",
        "Chassis types",
        "Nation histories",
        "Political background",
        "Military organizations",
        "Historical events",
        "Technology development"
    ] 