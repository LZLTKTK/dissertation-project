import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建图形和子图
fig, ax = plt.subplots(figsize=(12, 10))

# 定义各个阶段的内容
phases = [
    ('Preliminary Research', [
        '1. Analysis of Literature: Governmental and policy advisor reports, curriculum documents and pedagogical research',
        '2. Interviews: Meetings held with teachers, public engagement staff, SSERC staff, policy officers, science communicators and scientists',
        '3. Attendance at training events: SAW training event held in SynthSys "Supercytes Event" held at the QMRI'
    ]),
    ('Initial Design Phase', [
        'Primary School Activities: SAW Event',
        'Secondary School Activities: "Funding Conundrum", "Plasmid Builder"'
    ]),
    ('Implementation', [
        'SAW day at Victoria Primary School in Leith',
        'Trial run at "Biology Pupils in Labs" event'
    ]),
    ('Refinement of Material', [
        'Feedback and further meetings with teachers and advisors',
        'Refinement of activities and accompanying material'
    ])
]

# 绘制每个阶段的框和文字
y_start = 0.9
box_height = 0.1
for phase, activities in phases:
    # 绘制阶段框
    ax.add_patch(patches.FancyBboxPatch(
        (0.1, y_start), 0.8, box_height,
        boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightblue'
    ))
    ax.text(0.5, y_start + box_height / 2, phase, ha='center', va='center', fontsize=14, weight='bold')

    # 绘制活动内容
    y_activity = y_start - 0.05
    for activity in activities:
        ax.text(0.5, y_activity, activity, ha='center', va='center', fontsize=10)
        y_activity -= 0.03

    y_start -= 0.2

# 添加连接箭头
arrows = [
    ((0.5, 0.78), (0.5, 0.72)),
    ((0.5, 0.58), (0.5, 0.52)),
    ((0.5, 0.38), (0.5, 0.32))
]
for arrow in arrows:
    ax.annotate('', xy=arrow[1], xytext=arrow[0],
                arrowprops=dict(arrowstyle="->", lw=2))

# 设置标题
ax.set_title('Figure 2. Overview of Project', fontsize=16, pad=20)

# 隐藏坐标轴
ax.axis('off')

# 保存图形
plt.savefig('/root/working/00_Scripts/Figure_2_Overview_of_Project_Steps.png')

# 显示图形
plt.show()
