# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:51:29  sep. 16, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

oProject = oDesktop.NewProject()
oProject.SaveAs("D:/Users/JuanDavidMedellinC/Documents/Ansoft/antena_dipolo.aedt", True)
oProject.InsertDesign("HFSS", "DESIGN", "DrivenModal", "")

oDesign = oProject.SetActiveDesign("DESIGN")

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
					"Value:="		, "[327] mm"
				],
				[
					"NAME:radio_dipolo",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "array[0]/200"
				],
				[
					"NAME:radio_aire",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "radio_dipolo+(array[0]/4)"
				],
				[
					"NAME:gap_fuente",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				],
				[
					"NAME:longitud_res",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.475*array[0]"
				],
				[
					"NAME:longitud_dipolo",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "longitud_res/2-(gap_fuente/2)"
				],
				[
					"NAME:alto_aire",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "gap_fuente/2+longitud_dipolo+array[0]/10"
				]
			]
		]
	])

oEditor = oDesign.SetActiveEditor("3D Modeler")

# --- dipolo 1 ---
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "0.282842712474619mm",
		"Height:="		, "0.2mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
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
				"Cylinder1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "dipolo1"
				],
				[
					"NAME:Material",
					"Value:="		, "\"pec\""
				],
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 255,
					"B:="			, 255
				],
				[
					"NAME:Transparent",
					"Value:="		, 0
				],
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 255,
					"B:="			, 255
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
				"dipolo1:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Radius",
					"Value:="		, "radio_dipolo"
				],
				[
					"NAME:Height",
					"Value:="		, "longitud_dipolo"
				],
				[
					"NAME:Center Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "gap_fuente/2"
				]
			]
		]
	])

# --- dipolo 2 ---
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-30mm",
		"YCenter:="		, "-60mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "5mm",
		"Height:="		, "5mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
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
				"Cylinder1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "dipolo2"
				],
				[
					"NAME:Material",
					"Value:="		, "\"pec\""
				],
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 255,
					"B:="			, 255
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
				"dipolo2:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Center Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-gap_fuente/2"
				],
				[
					"NAME:Radius",
					"Value:="		, "radio_dipolo"
				],
				[
					"NAME:Height",
					"Value:="		, "-longitud_dipolo"
				]
			]
		]
	])

# --- aire ---
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-20mm",
		"YCenter:="		, "-100mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "14.142135623731mm",
		"Height:="		, "10mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
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
				"Cylinder1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "aire"
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
				"aire:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Center Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-alto_aire/2"
				],
				[
					"NAME:Radius",
					"Value:="		, "radio_aire"
				],
				[
					"NAME:Height",
					"Value:="		, "alto_aire"
				]
			]
		]
	])

# --- puerto ---
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "-80mm",
		"ZStart:="		, "70mm",
		"Width:="		, "10mm",
		"Height:="		, "-10mm",
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
					"Y:="			, "-radio_dipolo",
					"Z:="			, "-gap_fuente/2"
				],
				[
					"NAME:YSize",
					"Value:="		, "radio_dipolo*2"
				],
				[
					"NAME:ZSize",
					"Value:="		, "gap_fuente"
				]
			]
		]
	])

oModule = oDesign.GetModule("BoundarySetup")

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
					"Start:="		, ["1.00114875830296e-016mm","0mm","-0.5mm"],
					"End:="			, ["2.6092714079796e-016mm","0mm","0.5mm"]
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

oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["aire"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])

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
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "500MHz",
		"RangeEnd:="		, "1500MHz",
		"RangeStep:="		, "10MHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])

oProject.Save()