# Databricks notebook source
# MAGIC %md
# MAGIC # Content with notebooks
# MAGIC
# MAGIC You can also create content with Jupyter Notebooks. This means that you can include
# MAGIC code blocks and their outputs in your book.
# MAGIC
# MAGIC ## Markdown + notebooks
# MAGIC
# MAGIC As it is markdown, you can embed images, HTML, etc into your posts!
# MAGIC
# MAGIC ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# MAGIC
# MAGIC You can also $add_{math}$ and
# MAGIC
# MAGIC $$
# MAGIC math^{blocks}
# MAGIC $$
# MAGIC
# MAGIC or
# MAGIC
# MAGIC $$
# MAGIC \begin{aligned}
# MAGIC \mbox{mean} la_{tex} \\ \\
# MAGIC math blocks
# MAGIC \end{aligned}
# MAGIC $$
# MAGIC
# MAGIC But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# MAGIC
# MAGIC ## MyST markdown
# MAGIC
# MAGIC MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# MAGIC out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# MAGIC or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# MAGIC
# MAGIC ## Code blocks and outputs
# MAGIC
# MAGIC Jupyter Book will also embed your code blocks and output in your book.
# MAGIC For example, here's some sample Matplotlib code:

# COMMAND ----------

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

# COMMAND ----------

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);

# COMMAND ----------

# MAGIC %md
# MAGIC There is a lot more that you can do with outputs (such as including interactive outputs)
# MAGIC with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
