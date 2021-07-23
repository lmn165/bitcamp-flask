from pprint import pprint


def str_to_list(payload: str) -> []:
    return [i for i in payload]


# def reverseString(ls: []):
#     left, right =0, len(ls)-1
    # while left < right:
    #     ls[left], ls[right] = ls[right], ls[left]
    #     left += 1
    #     right -= 1
    # return ls

def reverseString(ls: []):
    return [ls[i] for i in range(len(ls)-1, -1, -1)]


def list_to_str(ls: []) -> []:
    return ''.join([i for i in ls])


if __name__ == '__main__':
    pprint(str_to_list("apple"))
    pprint(reverseString(str_to_list("apple")))
    print(list_to_str(reverseString(str_to_list("apple"))))