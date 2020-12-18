import random


# def random_operator(S, lst_op, total_ref):
#     while (True):
#         S_expression = ''
#         for i in range(0, len(S)):
#             if i == len(S)-1:
#                 S_expression = S_expression + S[i]
#             else:
#                 S_expression = S_expression + S[i] + random.choice(lst_op)
#
#         if eval(S_expression) == total_ref:
#             return S_expression

# S_expression = [['%s+' % i, '%s-' % i, '%s' % i] for i in S]
#     # S_expression = S_expression[:-1]
#     # print(L_a)
#     # # for i0 in S_expression[0]:
#     # #     for i1 in S_expression[1]:
#     # #         for i2 in S_expression[2]:
#     # #             for i3 in S_expression[3]:
#     # #                 for i4 in S_expression[4]:
#     # #                     for i5 in S_expression[5]:
#     # #                         for i6 in S_expression[6]:
#     # #                             for i7 in S_expression[7]:
#     # #                                 if eval(i0+i1+i2+i3+i4+i5+i6+i7+S[-1]) == total_ref:
#     # #                                     list_result.append(str(i0+i1+i2+i3+i4+i5+i6+i7+S[-1]))
#     #
#     # b = set(list_result)
#     # print(*list(b), sep='\n')


def list_expression(a, b, op):
    if b:
        for i in op:
            k = a + i + b[0]
            list_expression(k, b[1:], op)
    elif eval(a) == 100:
        print(a)


if __name__ == '__main__':
    S = str(123456789)
    op = ['+', '-', '']
    list_expression('1', '23456789', op)