import turtle

# 设置画笔
window = turtle.Screen()
window.bgcolor("black")  # 设置背景色
love = turtle.Turtle()
love.shape('turtle')
love.speed(2)  # 设置画笔速度
love.color('red', 'pink')
love.begin_fill()

# 绘制爱心
love.left(140)
love.forward(180)
love.circle(-100, 200)
love.left(120)
love.circle(-100, 200)
love.forward(180)

# 填充颜色
love.end_fill()

# 隐藏画笔
love.hideturtle()

# 等待用户关闭窗口
turtle.done()