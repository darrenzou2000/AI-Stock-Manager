class IdustryMapper:
    
    def __init__(self):
        self.industry = {
        "Agriculture, Forestry, Fish":
            {
                "Crops":
                    [
                        "Crops"
                    ],
                "Livestock & Animal Specialties":
                    [
                        "Livestock & Animal Specialties"
                    ],
                "Agricultural Services":
                    [
                        "Agricultural Services"
                    ],
                "Forestry":
                    [
                        "Forestry"
                    ],
                "Fishing, Hunting & Trapping":
                    [
                        "Fishing, Hunting & Trapping"
                    ]
            },
            
        "Mining":
            {
                "Metal Mining":
                    [
                        "Metal Mining","Gold & Silver Ores","Miscellaneous Metal Ores"
                    ],
                "Coal Mining":
                    [
                        "Bituminous Coal & Lignite Mining","Bituminous Coal & Lignite Surface Mining"
                    ],
                "Oil & Gas Extraction":
                    [
                        "Crude Petroleum & Natural Gas",
                        "Drilling Oil & Gas Wells",
                        "Oil & Gas Field Exploration Services",
                        "Oil & Gas Field Services"
                    ],
                "Mining Nonmetallic Minerals":
                    [
                        "Mining & Quarrying of Nonmetallic Minerals"
                    ]
                
            },
        "Construction":
            {
                "General Contractors & Builders":
                    [
                        "Residential Bldg Contractors","Operative Builders","Nonresidential Bldg Contractors",
                        "Asphalt Paving & Roofing Materials"
                    ],
                "Heavy Construction":
                    [
                        "Heavy Construction Non-Bldg Contractors","Water, Sewer, Pipeline, Comm & Power Line Construction"
                    ],
                "Special Trade Contractors":
                    [
                        "Special Trade Contractors",
                        "Electrical Work",
                    ]
               
            },
        "Manufacturing":
            {
                "Food":
                    [
                        "Food & Kindred Products",
                        "Meat Packing Plants",
                        "Sausages & Other Prepared Meat Products",
                        "Poultry Slaughtering & Processing",
                        "Dairy Products",
                        'Ice Cream & Frozen Desserts',
                        'Canned, Frozen & Preservd Fruit, Veg & Food Specialties',
                        'Canned, Fruits, Veg, Preserves, Jams & Jellies',
                        'Grain Mill Products',
                        'Bakery Products',
                        'Cookies & Crackers',
                        'Sugar & Confectionery Products',
                        'Fats & Oils',
                        'Beverages',
                        'Malt Beverages',
                        'Bottled & Canned Soft Drinks & C',
                        'Miscellaneous Food Preparations ',
                        'Prepared Fresh or Frozen Fish & Seafoods'
                    ],
                "Tobacco":
                    [
                        "Tobacco Products",
                        "Cigarettes"
                    ],
                "Textile Mill Products":
                    [
                        "Textile Mill Products",
                        "Broadwoven Fabric Mills, Cotton",
                        "Broadwoven Fabric Mills, Man Mad",
                        "Knitting Mills",
                        'Knit Outerwear Mills',
                        "Carpets & Rugs"
                    ],
                "Apparel":
                    [
                        "Apparel & Other Finishd Prods of Fabrics & Similar Matl",
                        "Men's & Boys' Furnishgs, Work Clothg, & Allied Garments",
                        "Women's, Misses', & Juniors Outerwear",
                        "Women's, Misses', Children's & Infants' Undergarments",
                        "Miscellaneous Fabricated Textile"
                    ],
                "Lumber":
                    [
                        "Lumber & Wood Products (No Furniture)",
                        "Sawmills & Planting Mills, General",
                        "Millwood, Veneer, Plywood, & Structural Wood Members",
                        "Mobile Homes",
                        "Prefabricated Wood Bldgs & Components"
                    ],
                "Furniture":
                    [
                        "Household Furniture",
                        'Wood Household Furniture, (No Upholstered)',
                        'Office Furniture',
                        'Office Furniture (No Wood)',
                        'Public Bldg & Related Furniture',
                        'Partitions, Shelvg, Lockers, & Office & Store Fixtures',
                        'Miscellaneous Furniture & Fixtures',         
                    ],
                "Paper":
                    [
                        'Papers & Allied Products',
                        'Pulp Mills',
                        'Paper Mills',
                        'Paperboard Mills',
                        'Paperboard Containers & Boxes',
                        'Converted Paper & Paperboard Prods (No Contaners/Boxes)',
                        'Plastics, Foil & Coated Paper Bags'
                    ],
                "Printing & Publishing":
                    [
                        "Newspapers: Publishing or Publishing & Printing",
                        "Periodicals: Publishing or Publishing & Printing",
                        "Books: Publishing or Publishing ",
                        "Book Printing",
                        "Miscellaneous Publishing",
                        "Commercial Printing",
                        "Manifold Business Forms",
                        "Greeting Cards",
                        "Blankbooks, Looseleaf Binders & Bookbindg & Relatd Work",
                        "Service Industries For The Printing Trade",
                    ],
                "Chemicals":
                    [
                        "Chemicals & Allied Products",
                        "Industrial Inorganic Chemicals",
                        "Plastic Material, Synth Resin/Rubber, Cellulos (No Glass)",
                        "Plastic Materials, Synth Resins & Nonvulcan Elastomers",
                        "Medicinal Chemicals & Botanical Products",
                        "Pharmaceutical Preparations",
                        "In Vitro & In Vivo Diagnostic Substances",
                        "Biological Products, (No Diagnostic Substances)",
                        "Soap, Detergents, Cleaning, Perfumes, Cosmetics",
                        "Specialty Cleaning, Polishing & Sanitation Preparations",
                        "Perfumes, Cosmetics & Other Toilet Preparations",
                        "Paints, Varnishes, Lacquers, Enamels",
                        "Industrial Organic Chemicals",
                        "Agricultural Chemicals",
                        "Miscellaneous Chemical Products",
                        "Adhesives & Sealants",
                    ],
                "Petroleum Refining":
                    [
                        "Petroleum Refining",
                        "Miscellaneous Products of Petroleum & Coal"
                    ],
                "Rubber & Plastic":
                    [
                        "Tires & Inner Tubes",
                        "Rubber & Plastics Footwear",
                        "Gaskets, Packg & Sealg Devices & Rubber & Plastics Hose",
                        "Fabricated Rubber Products",
                        "Miscellaneous Plastics Products",
                        "Unsupported Plastics Film & Sheet",
                        "Plastics Foam Products",
                        "Plastics Products"
                    ],
                "Leather":
                    [
                        "Leather & Leather Products",
                        "Footwear, (No Rubber)"

                    ],
                "Stone, Clay, Glass, & Concrete":
                    [
                        "Glass & Glassware, Pressed or Blown",
                        "Flat Glass",
                        "Glass Containers",
                        "Glass Products, Made of Purchased Glass",
                        "Cement, Hydraulic",
                        "Structural Clay Products",
                        "Pottery & Related Products",
                        "Concrete, Gypsum & Plaster Produ",
                        "Concrete Products, Except Block ",
                        "Cut Stone & Stone Products",
                        "Abrasive, Asbestos & Misc Nonmet",
                    ],
                "Primary Metal":
                    [
                        "Steel Works, Blast Furnaces & Rolling & Finishing Mills",
                        "Steel Works, Blast Furnaces & Rolling Mills (Coke Ovens)",
                        "Steel Pipe & Tubes",
                        "Iron & Steel Foundries",
                        "Primary Smelting & Refining of N",
                        "Primary Production of Aluminum",
                        "Secondary Smelting & Refining of",
                        "Rolling Drawing & Extruding of N",
                        "Drawing & Insulating of Nonferro",
                        "Nonferrous Foundries (Castings)",
                        "Miscellaneous Primary Metal Prod"
                    ],
                "Fabricated Metal Products":
                    [
                        "Metal Cans",
                        "Metal Shipping Barrels, Drums, K",
                        "Cutlery, Handtools & General Har",
                        "Hearing Equip, Except Elec & War",
                        "Heating Equipment, Except Electr",
                        "Fabricated Structural Metal Prod",
                        "Metal Doors, Sash, Frames, Moldi",
                        "Fabricated Plate Work (Boiler Sh",
                        "Sheet Metal Work",
                        "Prefabricated Metal Buildings & ",
                        "Screw Machine Products",
                        "Bolts, Nuts, Screws, Rivets & Wa",
                        "Metal Forgings & Stampings",
                        "Coating, Engraving & Allied Serv",
                        "Ordnance & Accessories, (No Vehi",
                        "Miscellaneous Fabricated Metal P",
                        
                    ],
                "Ind Machinery & Computers":
                    [
                        "Engines & Turbines",
                        "Farm Machinery & Equipment",
                        "Lawn & Garden Tractors & Home La",
                        "Construction, Mining & Materials",
                        "Construction Machinery & Equip",
                        "Mining Machinery & Equip (No Oil",
                        "Oil & Gas Field Machinery & Equi",
                        "Industrial Trucks, Tractors, Tra",
                        "Metalworkg Machinery & Equipment",
                        "Machine Tools, Metal Cutting Typ",
                        "Special Industry Machinery (No M",
                        "Printing Trades Machinery & Equi",
                        "Special Industry Machinery",
                        "General Industrial Machinery & E",
                        "Pumps & Pumping Equipment",
                        "Ball & Roller Bearings",
                        "Industrial & Commercial Fans & B",
                        "Industrial Process Furnaces & Ov",
                        "General Industrial Machinery & E",
                        "Computer & Office Equipment",
                        "Electronic Computers",
                        "Computer Storage Devices",
                        "Computer Terminals",
                        "Computer Communications Equipmen",
                        "Computer Peripheral Equipment",
                        "Calculating & Accounting Machine",
                        "Office Machines",
                        "Refrigeration & Service Industry",
                        "Air-Cond & Warm Air Heatg Equip ",
                        "Misc Industrial & Commercial Mac",

                    ],
                "Electronics":
                    [
                        'Electronic & Other Electrical Eq',
                        'Power, Distribution & Specialty ',
                        'Switchgear & Switchboard Apparat',
                        'Electrical Industrial Apparatus',
                        'Motors & Generators',
                        'Household Appliances',
                        'Electric Housewares & Fans',
                        'Electric Lighting & Wiring Equip',
                        'Household Audio & Video Equipmen',
                        'Phonograph Records & Prerecorded',
                        'Telephone & Telegraph Apparatus',
                        'Radio & Tv Broadcasting & Commun',
                        'Communications Equipment',
                        'Electronic Components & Accessor',
                        'Printed Circuit Boards',
                        'Semiconductors & Related Devices',
                        'Electronic Coils, Transformers &',
                        'Electronic Connectors',
                        'Electronic Components',
                        'Miscellaneous Electrical Machine',
                        'Magnetic & Optical Recording Med',
                    ],
                "Transportation Equipment":
                    [
                        'Motor Vehicles & Passenger Car B',
                        'Truck & Bus Bodies',
                        'Motor Vehicle Parts & Accessorie',
                        'Truck Trailers',
                        'Motor Homes',
                        'Aircraft & Parts',
                        'Aircraft',
                        'Aircraft Engines & Engine Parts',
                        'Aircraft Parts & Auxiliary Equip',
                        'Ship & Boat Building & Repairing',
                        'Railroad Equipment',
                        'Motorcycles, Bicycles & Parts',
                        'Guided Missiles & Space Vehicles',
                        'Miscellaneous Transportation Equ',
                    ],
                "Specialty Instruments":
                    [
                        'Search, Detection, Navigation, Guidance, Aeronautical Sys',
                        'Laboratory Apparatus & Furniture',
                        'Auto Controls For Regulating Res',
                        'Industrial Instruments For Measu',
                        'Totalizing Fluid Meters & Counti',
                        'Instruments For Meas & Testing o',
                        'Laboratory Analytical Instrument',
                        'Optical Instruments & Lenses',
                        'Measuring & Controlling Devices',
                        'Surgical & Medical Instruments &',
                        'Orthopedic, Prosthetic & Surgica',
                        'Dental Equipment & Supplies',
                        'X-Ray Apparatus & Tubes & Relate',
                        'Electromedical & Electrotherapeu',
                        'Ophthalmic Goods',
                        'Photographic Equipment & Supplie',
                        'Watches, Clocks, Clockwork Opera',
                    ],
                "Miscellaneous Manufacturing":
                    [
                        "Jewelry, Silverware & Plated War",
                        "Jewelry, Precious Metal",
                        "Musical Instruments",
                        "Dolls & Stuffed Toys",
                        "Games, Toys & Children's Vehicle",
                        "Sporting & Athletic Goods",
                        "Pens, Pencils & Other Artists' M",
                        "Costume Jewelry & Novelties",
                        "Miscellaneous Manufacturing Indu",
                    ]
        },
        "Transportation & Utilities":
            {
                "Railroads": 
                    [
                        "Railroads, Line-Haul Operating",
                        "Railroad Switching & Terminal Es",
                    ],
                "Passenger Road Transportation": 
                    [
                        "Local & Suburban Transit & Inter"
                    ],
                "Road Freight Transportation": 
                    [
                        "Trucking & Courier Services (No ",
                        "Trucking (No Local)",
                        "Public Warehousing & Storage",
                        "Terminal Maintenance Facilities ",
                    ],

                "Water Transportation": 
                    [
                        "Water Transportation",
                        "Deep Sea Foreign Transportation ",
                    ],
                "Air Transportation": 
                    [
                        "Air Transportation, Scheduled",
                        "Air Courier Services",
                        "Air Transportation, Nonscheduled",
                        "Airports, Flying Fields & Airpor",
                    ],
                "Pipelines": 
                    [
                       "Pipe Lines (No Natural Gas)"
                    ],
                "Transportation Services": 
                    [
                        "Transportation Services",
                        "Arrangement of Transportation of",
                    ],
                "Communications": 
                    [
                        "Radiotelephone Communications",
                        "Telephone Communications (No Rad",
                        "Telegraph & Other Message Commun",
                        "Radio Broadcasting Stations",
                        "Television Broadcasting Stations",
                        "Cable & Other Pay Television Ser",
                        "Communications Services",
                    ],
                "Electric, Gas, & Sanitary Svcs": 
                    [
                        "Electric, Gas & Sanitary Service",
                        "Electric Services",
                        "Natural Gas Transmission",
                        "Natural Gas Transmisison & Distr",
                        "Natural Gas Distribution",
                        "Electric & Other Services Combin",
                        "Gas & Other Services Combined",
                        "Water Supply",
                        "Sanitary Services",
                        "Refuse Systems",
                        "Hazardous Waste Management",
                        "Steam & Air-Conditioning Supply",
                        "Cogeneration Services & Small Po",
                    ]
            },
        "Wholesale Trade":
            {
                "Durable Goods": 
                    [
                       "Durable Goods",
                       "Motor Vehicles & Motor Vehicle P",
                       "Motor Vehicle Supplies & New Par",
                       "Furniture & Home Furnishings",
                       "Lumber & Other Construction Mate",
                       "Lumber, Plywood, Millwork & Wood",
                       "Professional & Commercial Equipm",
                       "Computers & Peripheral Equipment",
                       "Medical, Dental & Hospital Equip",
                       "Metals & Minerals (No Petroleum)",
                       "Metals Service Centers & Offices",
                       "Electrical Apparatus & Equipment",
                       "Electrical Appliances, Tv & Radi",
                       "Electronic Parts & Equipment",
                       "Hardware & Plumbing & Heating Eq",
                       "Hardware",
                       "Machinery, Equipment & Supplies",
                       "Construction & Mining (No Petro)",
                       "Industrial Machinery & Equipment",
                       "Misc Durable Goods",
                       "Jewelry, Watches, Precious Stone",
                       "Durable Goods",
                    ],
                "Nondurable Goods": 
                    [
                        "Paper & Paper Products",
                        "Drugs, Proprietaries & Druggists",
                        "Apparel, Piece Goods & Notions",
                        "Groceries & Related Products",
                        "Groceries, General Line",
                        "Farm Product Raw Materials",
                        "Chemicals & Allied Products",
                        "Petroleum Bulk Stations & Termin",
                        "Petroleum & Petroleum Products (",
                        "Beer, Wine & Distilled Alcoholic",
                        "Miscellaneous Nondurable Goods",
                    ],
            },
        "Retail Trade":
            {
                "Building Materials": 
                    [
                        "Building Materials, Hardware, Ga",
                        "Lumber & Other Building Material",
                        "Mobile Home Dealers",
                    ],
                "General Merchandise": 
                    [
                        "Department Stores",
                        "Variety Stores",
                        "Misc General Merchandise Stores",
                    ],
                "Grocery": 
                    [
                        "Food Stores",
                        "Grocery Stores",
                        "Convenience Stores",
                    ],
                "Auto Dealers & Service Stations": 
                    [
                        "Auto Dealers & Gasoline Stations",
                        "Auto & Home Supply Stores",
                    ],
                "Apparel & Accessory Stores": 
                    [
                        "Apparel & Accessory Stores",
                        "Women's Clothing Stores",
                        "Family Clothing Stores",
                        "Shoe Stores",
                    ],
                "Home Furniture": 
                    [
                        "Home Furniture, Furnishings & Eq",
                        "Furniture Stores",
                        "Radio, Tv & Consumer Electronics",
                        "Computer & Computer Software Sto",
                        "Record & Prerecorded Tape Stores",
                    ],
                "Eating & Drinking Places": 
                    [
                        "Eating & Drinking Places",
                        "Eating Places",
                    ],
                "Miscellaneous Retail": 
                    [
                        "Miscellaneous Retail",
                        "Drug Stores & Proprietary Stores",
                        "Miscellaneous Shopping Goods Sto",
                        "Jewelry Stores",
                        "Hobby, Toy & Game Shops",
                        "Nonstore Retailers",
                        "Catalog & Mail-Order Houses",
                        "Retail Stores",
                    ],
            },
            "Financial":
                {
                    "Depository Institutions": 
                        [
                            "American Depositary Receipts",
                            "National Commercial Banks",
                            "State Commercial Banks",
                            "Commercial Banks",
                            "Savings Institution, Federally C",
                            "Savings Institutions, Not Federa",
                            "Functions Related to Depository ",
                        ],
                    "Non-depository Credit Inst": 
                        [
                            "Federal & Federally-Sponsored Cr",
                            "Personal Credit Institutions",
                            "Short-Term Business Credit Insti",
                            "Miscellaneous Business Credit In",
                            "Mortgage Bankers & Loan Correspo",
                            "Loan Brokers",
                            "Finance Lessors",
                            "Asset-Backed Securities",
                            "Finance Services",
                        ],
                    "Security & Commodity Brokers": 
                        [
                            "Security & Commodity Brokers, De",
                            "Security Brokers, Dealers & Flot",
                            "Commodity Contracts Brokers & De",
                            "Investment Advice",
                        ],
                    "Insurance Carriers": 
                        [
                            "Life Insurance",
                            "Accident & Health Insurance",
                            "Hospital & Medical Service Plans",
                            "Fire, Marine & Casualty Insuranc",
                            "Surety Insurance",
                            "Title Insurance",
                            "Insurance Carriers",
                        ],
                    "Insurance Agents": 
                        [
                            "Insurance Agents, Brokers & Serv"
                        ],
                    "Real Estate": 
                        [
                            "Real Estate",
                            "Real Estate Operators (No Develo",
                            "Operators of Nonresidential Buil",
                            "Operators of Apartment Buildings",
                            "Lessors of Real Property",
                            "Real Estate Agents & Managers (F",
                            "Real Estate Dealers (For Their O",
                            "Land Subdividers & Developers (N",
                        ],
                    "Holding & Investment Offices": 
                        [
                            "Blank Checks",
                            "Oil Royalty Traders",
                            "Patent Owners & Lessors",
                            "Mineral Royalty Traders",
                            "Real Estate Investment Trusts",
                            "Investors",
                        ],
                },
        "Services":
            {
                "Hotels": 
                    [
                        "Hotels, Rooming Houses, Camps & ",
                        "Hotels & Motels",
                    ],
                "Personal Services": 
                    [
                            "Personal Services"
                    ],
                "Business Services": 
                    [
                        "Advertising",
                        "Advertising Agencies",
                        "Consumer Credit Reporting, Colle",
                        "Mailing, Reproduction, Commercia",
                        "Direct Mail Advertising Services",
                        "To Dwellings & Other Buildings",
                        "Miscellaneous Equipment Rental &",
                        "Equipment Rental & Leasing",
                        "Employment Agencies",
                        "Help Supply Services",
                        "Computer Programming, Data Proce",
                        "Computer Programming Services",
                        "Prepackaged Software",
                        "Computer Integrated Systems Desi",
                        "Computer Processing & Data Prepa",
                        "Computer Rental & Leasing",
                        "Miscellaneous Business Services",
                        "Detective, Guard & Armored Car S",
                        "Photofinishing Laboratories",
                        "Telephone Interconnect Systems",
                        "Business Services",
                    ],
                "Automotive Repair": 
                    [
                        "Automotive Repair, Services & Pa",
                        "Auto Rental & Leasing (No Driver",
                    ],
                "Miscellaneous Repair": 
                    [
                        "Miscellaneous Repair Services"
                    ],
                "Motion Pictures": 
                    [
                        "Motion Picture & Video Tape Prod",
                        "Allied to Motion Picture Product",
                        "Motion Picture & Video Tape Dist",
                        "Allied to Motion Picture Distrib",
                        "Motion Picture Theaters",
                        "Video Tape Rental",
                    ],
                "Amusement & Rec Svcs": 
                    [
                        "Amusement & Recreation Services",
                        "Racing, Including Track Operatio",
                        "Miscellaneous Amusement & Recrea",
                        "Membership Sports & Recreation C",
                    ],
                "Health Services": 
                    [
                        "Health Services",
                        "Offices & Clinics of Doctors of ",
                        "Nursing & Personal Care Faciliti",
                        "Skilled Nursing Care Facilities",
                        "Hospitals",
                        "General Medical & Surgical Hospi",
                        "Medical Laboratories",
                        "Home Health Care Services",
                        "Misc Health & Allied Services",
                        "Specialty Outpatient Facilities",
                    ],
                "Legal Services": 
                    [
                        "Legal Services"
                    ],
                "Educational Services": 
                    [
                        "Educational Services"
                    ],
                "Social Services": 
                    [
                        "Social Services",
                        "Child Day Care Services",
                    ],
                "Membership Organizations": 
                    [
                        "Membership Organizations"
                    ],
                "Engr, Acct, Rsrch, Mgmt Svcs": 
                    [
                        "Engineering, Accounting, Researc",
                        "Engineering Services",
                        "Commercial Physical & Biological",
                        "Testing Laboratories",
                        "Management Services",
                        "Management Consulting Services",
                        "Facilities Support Management Se",
                    ],
                "Miscellaneous Services": 
                    [
                        "Services"
                    ],    
            },
        "Closed-End Funds":
            {
                    "Closed-End Funds":["Closed-End Funds"]   
            },
        "Unknown":
            {
                "Unknown":
                    [
                        "Non-Operating Establishments"
                    ]
            }
        }
        self.mappedIndustry = {}
        for sector,subsectors in self.industry.items():
            for subSectorName, industries in subsectors.items():
                for industry in industries:
                    self.mappedIndustry[industry]={"sector":sector,"subsector":subSectorName}
                    
                
                
    def getSectorAndSubsector(self,input):
        if(input in self.mappedIndustry):return self.mappedIndustry[input]
        
        for i in range(len(input)):
            shortenedInput = input[0:-i]
            if(shortenedInput in self.mappedIndustry):return self.mappedIndustry[shortenedInput]
        print("found no industry for ",input)
        return None
