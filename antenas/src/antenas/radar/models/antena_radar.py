# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 17:19:37  dic. 23, 2025
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.SaveAs("D:/Users/JuanDavidMedellinC/Documents/Ansoft/PATCH_ANTENNA.aedt", True)
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
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
					"Value:="		, "[11, 18, 2.5, 5.6, 7.36, 8.28, 2.7, 3.5, 1.8, 18, 41, 48, 1.57, 0.017, 1.57] mm"
				],
				[
					"NAME:center_antenna_Y",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "(array[10]-array[0])/2"
				],
				[
					"NAME:center_antenna_X",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "(array[11]-array[1])/2"
				]
			],
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
		"YSize:="		, "1.4mm",
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
					"Value:="		, "sustrato_antena"
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
					"Value:="		, 0.4
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.6
				],
				[
					"NAME:Name",
					"Value:="		, "sustrato_reflector"
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
				"sustrato_reflector:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-array[9]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[10]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[11]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-array[14]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[11]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[10]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "8mm",
		"YSize:="		, "6mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "tierra_reflector"
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
				"tierra_reflector:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-array[9]"
				],
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-array[9]-array[14]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[11]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[10]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[13]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "10mm",
		"YSize:="		, "8mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "sustrato_antena"
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
					"Value:="		, 0.6
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
				"sustrato_antena:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[0]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[12]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "8mm",
		"YSize:="		, "8mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "tierra_antena"
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
				"tierra_antena:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[11]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[10]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[13]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-array[13]"
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
				"tierra_antena:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "array[1]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[0]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "6mm",
		"YSize:="		, "6mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "tierra_antena_2"
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
				"tierra_antena_2:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "0mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-array[13]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[1]-array[2]-array[3]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[0]-array[6]"
				],
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[2]",
					"Y:="			, "center_antenna_Y+array[0]-array[6]",
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
				"tierra_antena_2:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[2]",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "tierra_antena_2",
		"Tool Parts:="		, "tierra_antena"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oDesign.Undo()
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "tierra_antena",
		"Tool Parts:="		, "tierra_antena_2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "6mm",
		"YSize:="		, "6mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "alimantacion_antena"
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
				"alimantacion_antena:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "array[12]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[1]-array[2]-array[5]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[8]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[12]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[13]"
				],
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[2]+array[5]",
					"Y:="			, "center_antenna_Y+array[0]-array[7]-array[8]",
					"Z:="			, "array[12]"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "8mm",
		"YSize:="		, "8mm",
		"ZSize:="		, "2mm"
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
					"Value:="		, "parche_antena"
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
				"parche_antena:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "array[12]"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[5]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[4]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "array[13]"
				],
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[2]",
					"Y:="			, "center_antenna_Y+array[0]-array[6]-array[4]",
					"Z:="			, "array[12]"
				]
			]
		]
	])
oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "parche_antena",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [218],
			"Vertices:="		, [],
			"Radius:="		, "array[4]",
			"Setback:="		, "0mm"
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "6mm",
		"Height:="		, "4mm",
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
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 128,
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
				"puerto:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[1]",
					"Y:="			, "center_antenna_Y",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[1]",
					"Y:="			, "center_antenna_Y+array[0]-array[6]-(array[8]/2)-(6/2)",
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
				"puerto:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[1]",
					"Y:="			, "center_antenna_Y",
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
				"puerto:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[1]",
					"Y:="			, "center_antenna_Y+array[0]-array[7]-(array[8]/2)-(6/2)",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "center_antenna_X+array[1]",
					"Y:="			, "center_antenna_Y+array[0]-array[7]-(array[8]/2)-(6mm/2)",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "8mm",
		"YSize:="		, "8mm",
		"ZSize:="		, "6mm"
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
				"aire:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-array[9]-array[14]-array[13]-4mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "array[11]"
				],
				[
					"NAME:YSize",
					"Value:="		, "array[10]"
				],
				[
					"NAME:ZSize",
					"Value:="		, "(array[9]-array[14]-array[13]-4mm)*2"
				],
				[
					"NAME:ZSize",
					"Value:="		, "(array[9]+array[14]+array[13]+4mm)*2"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["aire"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["puerto"],
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
					"Start:="		, ["33mm","21.6mm","6.66133814775094e-016mm"],
					"End:="			, ["33mm","21.6mm","4mm"]
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
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "7.5GHz",
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
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "1GHz",
		"RangeEnd:="		, "15GHz",
		"RangeStep:="		, "10MHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oProject.Save()
