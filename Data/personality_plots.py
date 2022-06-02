import random
import numpy as np
import matplotlib.pyplot as plt

for i in range(0, 50):
    data = {}
    for dim in ['Dominant', 'Influential', 'Steady', 'Compliant']:
        data[dim] = random.randint(0, 100)

    dims = list(data.keys())
    values = list(data.values())  

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(dims, values, color =['red', 'yellow', 'green', 'blue'],
            width = 0.4)
    
    plt.ylabel("Score")
    plt.title("DISC-profile")

    plt.savefig(f'Data/personality_plots/{i}_personality.png')




