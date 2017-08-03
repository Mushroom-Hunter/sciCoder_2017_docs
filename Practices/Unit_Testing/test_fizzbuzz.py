#!/usr/bin/env python

from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    """
    """
    idx_arr = list(range(1,6))
    out_arr = [1,2,'fizz',4,'buzz']
    # Call the function
    out_arr_1 = [fizzbuzz(x) for x in idx_arr]
    # Assert
    assert(out_arr_1 == out_arr)



# def test_fizzbuzz_1():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(1)
#     assert(sample_x_1==1)

# def test_fizzbuzz_2():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(2)
#     assert(sample_x_1==2)

# def test_fizzbuzz_3():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(3)
#     assert(sample_x_1=='fuzz')

# def test_fizzbuzz_4():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(4)
#     assert(sample_x_1==4)

# def test_fizzbuzz_5():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(5)
#     assert(sample_x_1=='buzz')

# def test_fizzbuzz_6():
#     """
#     Tests the output of the function `fuzzbuzz`
#     """
#     sample_x_1 = fizzbuzz(6)
#     assert(sample_x_1==6)

# # def test_type():
# #     """
# #     """
# #     sample_x_1 = fizzbuzz(sample_x)
# #     assert(type(sample_x)==type(sample_x_1))
