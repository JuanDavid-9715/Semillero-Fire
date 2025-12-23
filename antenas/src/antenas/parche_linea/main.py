import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    from perseo_optimizer import commands, interface
    from dotenv import load_dotenv
    
    load_dotenv()
    
    ansys_path = os.getenv('ANSYS_PATH')  # Please change this path for your Ansys path
    save_path = os.getenv('SAVE_PATH')  # Please change this path for your default Ansys save path
    cat = "Line antenna"
    sub_cat = "Line"
    pro = "antena_linea"
    des = "HFSSDesign1"
    var = "array"
    u = "mm"
    val_max = [1.57, 110, 70, 0.017, 10]
    val_min = [1.57, 110, 70, 0.017, 1]
    val_nom = [1.57, 110, 70, 0.017, 3]
    i = 1
    p = 1
    b = 0
    desc = "Patch antenna working in 2.6GHz adapted minimum to -10dB"
    rep = {"SMN": [(1, 1)], "additional_data": {"fmin": 1.5, "points": 201, "units": "GHz"}}


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
            fit_value = ((2.4 - work_freq) / 2.4)**2

        # RETURN CALCULATED VALUE
        return fit_value


    commands.init_system(
        ansys_path, save_path, pro, des, var, u, val_max, val_min, val_nom, i, p, b, rep, cat, sub_cat, desc
    )
    interface.main_menu(function_fitness)  # FIRST INITIALIZE THE SYSTEM AND LATER RUN THE MAIN MENU
    
if __name__ == "__main__":
    main()