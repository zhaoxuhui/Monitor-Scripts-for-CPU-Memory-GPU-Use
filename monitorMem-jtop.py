from jtop import jtop


if __name__ == "__main__":

    print("Simple jtop memory reader")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            # Print all cpu
            for name, data in jetson.memory.items():
                print("------ {name} ------".format(name=name))
                print(data)
