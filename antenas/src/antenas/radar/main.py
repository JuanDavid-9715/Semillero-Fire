import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    from perseo_optimizer import commands, interface
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # --- CONFIGURATION PARAMETERS ---    
    ANSYS_INSTALL_PATH = os.getenv('ANSYS_PATH')  # Please change this path for your Ansys path
    ANSYS_PROJECT_SAVE_PATH = os.getenv('SAVE_PATH')  # Please change this path for your default Ansys save path
    
    PROJECT_CATEGORY = "Radar antenna"
    PROJECT_SUBCATEGORY = "Radar"
    PROJECT_DESCRIPTION  = "Radar antenna working in 7.5GHz adapted minimum to -10dB"
    
    PROJECT_NAME = "antena_radar"
    HFSS_DESIGN_NAME = "HFSSDesign1"
    
    VARIABLE_ARRAY_NAME = "array"
    UNITS = "mm"
    
    ITERATIONS = 1
    PARTICLES = 1
    BRANCHES = 0
    
    """
    Antenna Parameter Array Structure (15 variables in order):
    
    [Xs, Ys, Y1, Y2, X1, X2, X3, X4, Xf, S, Xr, Yr, Hs, H, Hr1]
    
    Where:
    
    PATCH ANTENNA (Radiating Element):
        Xs  : Patch width (mm)
        Ys  : Patch length/height (mm)
        Hs  : Substrate thickness (mm)
        Xf  : Feed line width (mm)
        Y1, Y2, X1-X4 : Additional patch geometry parameters
    
    REFLECTOR (Ground Plane / Backing Structure):
        S   : Separation distance between antenna and reflector (mm)
        Xr  : Reflector width (mm)
        Yr  : Reflector height (mm)
        Hr1 : Reflector substrate thickness (mm)
    
    COMMON:
        H   : Conductor thickness (mm) - Typically very small (0.017mm ≈ 0.5oz copper)
    """
    
                        #Xs, Ys, Y1, Y2, X1, X2, X3, X4, Xf, S, Xr, Yr, Hs, H, Hr1
    NOMINAL_VALUES =    [11, 18, 2.5, 5.6, 7.36, 8.28, 2.7, 3.5, 1.8, 18, 41, 48, 1.57, 0.017, 1.57]
    MAX_VALUES =        [11, 18, 2.5, 5.6, 7.36, 8.28, 2.7, 3.5, 1.8, 18, 41, 48, 1.57, 0.017, 1.57]
    MIN_VALUES =        [11, 18, 2.5, 5.6, 7.36, 8.28, 2.7, 3.5, 1.8, 18, 41, 48, 1.57, 0.017, 1.57]
    
    """
    Simulation Request Configuration:
    
    The 'rep' dictionary defines what HFSS should simulate and return.
    
    Structure:
        SMN (S-Matrix Network): 
            - [(1, 1)] requests the S11 parameter (port 1 to port 1)
        
        additional_data:
            - fmin: Starting frequency (GHz)
            - points: Number of frequency points in the sweep
            - units: Frequency units for the simulation
    """
    SIMULATION_REQUESTS = {
        "SMN": [(1, 1)],
        "additional_data": {
            "fmin": 1,
            "points": 1400,
            "units": "GHz"
        }
    }


    def function_fitness(dataReports):
        # PRESENT THE REPORTS THAT HFSS  GENERATE
        for key in dataReports:
            print(str(key) + "--->" + str(len(dataReports[key])))

        # FIST FILTER TO GET ONLY DATA UNDER db <= -10
        freq = [
            dataReports['S11'][index][0] for index in range(len(dataReports["S11"])) if dataReports["S11"][index][1] <= -10
        ]
        dB = [
            dataReports['S11'][index][1] for index in range(len(dataReports["S11"])) if dataReports["S11"][index][1] <= -10
        ]

        if len(freq) == 0 or len(dB) == 0:
            # PENALTY THE FIT VALUE
            fit_value = 10

        else:
            # FIND THE WORK FREQUENCY AND POWER OF ANTENNA
            dB_min = min(dB)
            work_freq = freq[dB.index(dB_min)]

            # CALCULATE THE FIT VALUE
            fit_value = ((7 - work_freq) / 7)**2

        # RETURN CALCULATED VALUE
        return fit_value


    commands.init_system(
        ansys_exe=ANSYS_INSTALL_PATH,
        ansys_save_def=ANSYS_PROJECT_SAVE_PATH,
        project_name=PROJECT_NAME,
        design_name=HFSS_DESIGN_NAME,
        variable_name=VARIABLE_ARRAY_NAME,
        units=UNITS, 
        max=MAX_VALUES, 
        min=MIN_VALUES, 
        nominals=NOMINAL_VALUES, 
        iterations=ITERATIONS, 
        particles=PARTICLES,
        branches=BRANCHES, 
        reports=SIMULATION_REQUESTS, 
        category=PROJECT_CATEGORY, 
        sub_category=PROJECT_SUBCATEGORY, 
        description=PROJECT_DESCRIPTION
    )
    interface.main_menu(function_fitness)  # FIRST INITIALIZE THE SYSTEM AND LATER RUN THE MAIN MENU
    

if __name__ == "__main__":
    main()