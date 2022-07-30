# libraries
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# use the venn2 function
venn2(subsets=(10, 5, 2), set_labels=('Group A', 'Group B'))
# showing plot
plt.show()
