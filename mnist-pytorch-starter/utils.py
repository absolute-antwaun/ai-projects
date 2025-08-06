import matplotlib.pyplot as plt

def plot_sample(images, labels):
    fig, ax = plt.subplots(1, 6, figsize=(12, 2))
    for i in range(6):
        ax[i].imshow(images[i].squeeze(), cmap="gray")
        ax[i].set_title(f"Label: {labels[i]}")
        ax[i].axis('off')
    plt.tight_layout()
    plt.show()
