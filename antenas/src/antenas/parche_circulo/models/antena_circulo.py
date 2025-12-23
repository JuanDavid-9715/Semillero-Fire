# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 1:46:34  sep. 03, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("antena_circulo")
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
					"Value:="		, "[1.57, 110, 70, 15, 0.017, 15] m"
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
		"XSize:="		, "0.8mm",
		"YSize:="		, "0.8mm",
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
					"Value:="		, "sutrato"
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
				"sutrato:CreateBox:1"
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
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "50mm",
		"YCenter:="		, "-50mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "20mm",
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
					"Value:="		, "parche"
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
				"parche:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Radius",
					"Value:="		, "array[5]"
				],
				[
					"NAME:Height",
					"Value:="		, "array[4]"
				],
				[
					"NAME:Center Position",
					"X:="			, "array[2]/2",
					"Y:="			, "array[2]/2",
					"Z:="			, "array[0]"
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
				"parche:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Center Position",
					"X:="			, "array[1]/2",
					"Y:="			, "array[1]/2",
					"Z:="			, "array[0]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "20mm",
		"YPosition:="		, "-60mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "50mm",
		"YSize:="		, "10mm",
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
					"Value:="		, "trans"
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
				"trans:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "array[4]"
				],
				[
					"NAME:YSize",
					"Value:="		, "0.72mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "((array[1]/2)-array[5])-array[3]"
				],
				[
					"NAME:Position",
					"X:="			, "(array[1]/2)+array[5]",
					"Y:="			, "(array[1]/2)-(0.72mm/2)",
					"Z:="			, "array[4]"
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
				"trans:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "(array[1]/2)+array[5]",
					"Y:="			, "(array[1]/2)-(0.72mm/2)",
					"Z:="			, "array[0]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "25mm",
		"YPosition:="		, "-50mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "15mm",
		"YSize:="		, "10mm",
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
					"Value:="		, "energia"
				],
				[
					"NAME:Name",
					"Value:="		, "alimentacion"
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
				"alimentacion:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "4.84mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[0]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[3]"
				],
				[
					"NAME:Position",
					"X:="			, "array[1]-array[3]",
					"Y:="			, "(array[1]/2)-(4.84/2)",
					"Z:="			, "array[0]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[4]"
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
				"alimentacion:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "array[1]-array[3]",
					"Y:="			, "(array[1]/2)-(4.84mm/2)",
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
					"Y:="			, "-75mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "array[3]/2"
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
					"Value:="		, "array[2]"
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
					"Z:="			, "array[2]/2"
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
					"Z:="			, "-array[2]/2"
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
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "25mm",
		"ZStart:="		, "50mm",
		"Width:="		, "25mm",
		"Height:="		, "-15mm",
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
					"NAME:YSize",
					"Value:="		, "50mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "15mm"
				],
				[
					"NAME:Position",
					"X:="			, "array[2]",
					"Y:="			, "(array[2]/2)-25",
					"Z:="			, "0mm"
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
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "array[2]",
					"Y:="			, "(array[2]/2)-25mm",
					"Z:="			, "0mm"
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
				"Rectangle1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "array[1]",
					"Y:="			, "(array[1]/2)-25mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "array[0]",
					"Y:="			, "(array[1]/2)-25mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "array[1]",
					"Y:="			, "(array[1]/2)-25mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oModule.AssignWavePort(
	[
		"NAME:1",
		"Objects:="		, ["Rectangle1"],
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
					"Start:="		, ["110mm","55mm","5.55111512312578e-015mm"],
					"End:="			, ["110mm","55mm","1.587mm"]
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
