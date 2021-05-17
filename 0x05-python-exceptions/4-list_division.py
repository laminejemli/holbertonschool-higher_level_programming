#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divis = []
    tmp = 0
    for l in range(0, list_length):
        try:
            tmp = my_list_1[l] / my_list_2[l]
        except TypeError:
            tmp = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        except IndexError:
            tmp = 0
            print("out of range")
        finally:
            pass
        divis.append(tmp)
    return divis
