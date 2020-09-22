import time
import multiprocessing

# square_result = []

def calc_square(numbers):
    for i in numbers:
        time.sleep(0.3)
        print('square ' + str(i*i))
    #     square_result.append(str(i*i))
    # print(square_result)

def calc_cube(numbers):
    for i in numbers:
        time.sleep(0.3)
        print('cube ' + str(i*i*i))

if __name__ == '__main__':
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # print(str(square_result))
    print("Done!")
