# -*- coding: utf-8 -*-
# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 18:59:47  oct. 18, 2025
# ----------------------------------------------
import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.Rename("D:/Users/JuanDavidMedellinC/Documents/Ansoft/antena_ranura_elemental.aedt", True)
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.RenameDesignInstance("HFSSDesign1", "DESIGN")

oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers", 
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:array",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "[327.8, 1500, 0.5, 800] mm"
                ],
                [
                    "NAME:placa",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "(array[1]*array[0]) m"  
                ],
                [
                    "NAME:grosor_placa", 
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "(array[2]) m" 
                ],
                [
                    "NAME:ancho_ranura",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True, 
                    "Value:=", "(array[0]/50) m" 
                ],
                [
                    "NAME:alto_ranura",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "(array[3]*array[0]) m"  
                ],
                [
                    "NAME:aire",
                    "PropType:=", "VariableProp", 
                    "UserDef:=", True,
                    "Value:=", "(2*array[0]) m" 
                ],
                [
                    "NAME:profundo_aire",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "0.150 m" 
                ],
                [
                    "NAME:alto_puerto",
                    "PropType:=", "VariableProp", 
                    "UserDef:=", True,
                    "Value:=", "0.002 m" 
                ]
            ]
        ]
    ])

oEditor = oDesign.SetActiveEditor("3D Modeler")
# Placa y ranura
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "1mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "1.2mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"pec\""
				],
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 128,
					"B:="			, 128
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "-placa/2",
					"Z:="			, "-placa/2"
				],
				[
					"NAME:XSize",
					"Value:="		, "grosor_placa"
				],
				[
					"NAME:YSize",
					"Value:="		, "placa"
				],
				[
					"NAME:ZSize",
					"Value:="		, "placa"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "-400mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "150mm",
		"YSize:="		, "100mm",
		"ZSize:="		, "150mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box2:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "-ancho_ranura/2",
					"Z:="			, "-alto_ranura/2"
				],
				[
					"NAME:XSize",
					"Value:="		, "grosor_placa"
				],
				[
					"NAME:YSize",
					"Value:="		, "ancho_ranura"
				],
				[
					"NAME:ZSize",
					"Value:="		, "alto_ranura"
				]
			]
		]
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Box1",
		"Tool Parts:="		, "Box2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

# aire
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-250mm",
		"YPosition:="		, "-500mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "250mm",
		"YSize:="		, "150mm",
		"ZSize:="		, "150mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box3",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box3"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"air\""
				],
				[
					"NAME:Color",
					"R:="			, 192,
					"G:="			, 192,
					"B:="			, 192
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.8
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box3:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-profundo_aire/2",
					"Y:="			, "-aire/2",
					"Z:="			, "-aire/2"
				],
				[
					"NAME:XSize",
					"Value:="		, "profundo_aire"
				],
				[
					"NAME:YSize",
					"Value:="		, "aire"
				],
				[
					"NAME:ZSize",
					"Value:="		, "aire"
				]
			]
		]
	])
oProject.Save()

# puerto
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "-450mm",
		"ZStart:="		, "250mm",
		"Width:="		, "100mm",
		"Height:="		, "-100mm",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "-ancho_ranura/2",
					"Z:="			, "-alto_puerto/2"
				],
				[
					"NAME:YSize",
					"Value:="		, "ancho_ranura"
				],
				[
					"NAME:ZSize",
					"Value:="		, "alto_puerto"
				]
			]
		]
	])

oProject.Save()
oModule = oDesign.GetModule("BoundarySetup")
#radiación
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Box3"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oProject.Save()
#lumped port
oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["Rectangle1"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["1.60812264967664e-019mm","-0.003278mm","0mm"],
					"End:="			, ["5.62251485728166e-019mm","0.003278mm","1.51788304147971e-018mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"Impedance:="		, "50ohm"
	])

oProject.Save()
# simulación
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "2GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 20,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"RayDensityPerWavelength:=", 4,
		"MaxNumberOfBounces:="	, 5,
		"InfiniteSphereSetup:="	, -1
	])
oProject.Save()
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "500MHz",
		"RangeEnd:="		, "2000MHz",
		"RangeStep:="		, "10MHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])

oProject.Save()