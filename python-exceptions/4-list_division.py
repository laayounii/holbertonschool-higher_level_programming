#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for i in range(0, list_length):
        try:
            y = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            y = 0
        except ZeroDivisionError:
            print("division by 0")
            y = 0
        except IndexError:
            print("out of range")
            y = 0
        except Exception as e:
            pass
        finally:
            x.append(y)
    return (x)
