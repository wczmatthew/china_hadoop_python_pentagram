"""
    作者：wcz
    功能：五角星的绘制
    版本：V1.0
    日期：22/06/2018
    新增：循环绘制增长边长的五角星
    新增：使用迭代
"""


import turtle


def draw_recursive_pentagram(size):
    """
            绘制五角星
        """
    # 绘制五角星
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1

    if size <= 100:
        size += 10
        draw_recursive_pentagram(size)


def draw_pentagram(size):
    """
        绘制五角星
    """
    # 绘制五角星
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1


def main():
    """
        主函数
    """

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pencolor('red')

    size = 50
    # 迭代绘制五角星
    draw_recursive_pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()