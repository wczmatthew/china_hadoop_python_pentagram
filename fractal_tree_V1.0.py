"""
    作者：wcz
    功能：五角星的绘制
    版本：V1.0
    日期：22/06/2018
    新增：利用递归绘制分型树
"""


import turtle

BRANCH_COLOR = 'brown'
LEAF_COLOR = 'green'


def draw_branch(branch_length):
    """
        绘制分型树
    """
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)

        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)

        # 返回之前的树枝路径
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    """
        主函数
    """
    turtle.penup()
    turtle.left(90)
    turtle.backward(80)
    turtle.right(90)

    turtle.pendown()

    turtle.left(90)

    draw_branch(100)

    turtle.exitonclick()


if __name__ == '__main__':
    main()