# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 20:52:26  sep. 06, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("antena_linea")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
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
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[1.57, 110, 70, 0.017, 3] m"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "1.4mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "0.2mm"
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
					"NAME:Name",
					"Value:="		, "sustrato"
				],
				[
					"NAME:Material",
					"Value:="		, "\"FR4_epoxy\""
				],
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 64,
					"B:="			, 0
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
				"sustrato:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[0]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "-25mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "25mm",
		"YSize:="		, "15mm",
		"ZSize:="		, "5mm"
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
					"NAME:Name",
					"Value:="		, "linea"
				],
				[
					"NAME:Material",
					"Value:="		, "\"copper\""
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
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
				"linea:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "array[4]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[3]"
				],
				[
					"NAME:Position",
					"X:="			, "(array[1]/2)-(array[4]/2)",
					"Y:="			, "0mm",
					"Z:="			, "array[0]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "25mm",
		"YPosition:="		, "-75mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "25mm",
		"YSize:="		, "25mm",
		"ZSize:="		, "10mm"
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
					"NAME:Name",
					"Value:="		, "air"
				],
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
				"air:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-array[2]/2"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "150mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "75mm",
		"Width:="		, "-20mm",
		"Height:="		, "-50mm",
		"WhichAxis:="		, "Y"
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
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "puerto"
				],
				[
					"NAME:Name",
					"Value:="		, "puerto1"
				],
				[
					"NAME:Color",
					"R:="			, 64,
					"G:="			, 0,
					"B:="			, 128
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.5
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
				"puerto1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "50mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "20mm"
				],
				[
					"NAME:Position",
					"X:="			, "(array[1]/2)-(50/2)",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "puerto1"
	])
oEditor.Paste()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"puerto2:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "(array[1]/2)-(50mm/2)",
					"Y:="			, "array[1]",
					"Z:="			, "0mm"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Faces:="		, [8],
		"InfGroundPlane:="	, False
	])
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["air"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule.AssignWavePort(
	[
		"NAME:1",
		"Objects:="		, ["puerto1"],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["55mm","2.4894981252574e-015mm","-4.59242549680257e-015mm"],
					"End:="			, ["55mm","0mm","1.587mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oModule.AssignWavePort(
	[
		"NAME:2",
		"Objects:="		, ["puerto2"],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["55mm","110mm","-4.59242549680257e-015mm"],
					"End:="			, ["55mm","110mm","1.587mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "5GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 2,
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
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "1500MHz",
		"RangeEnd:="		, "3500MHz",
		"RangeCount:="		, 200,
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
