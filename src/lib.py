"""
Main cli or app entry point
"""
import pandas as pd
import matplotlib.pyplot as plt


# Calculate the descriptive statistics
def head(data):
    population_head = data[0:6]
    return population_head


def mean(data):
    population_stats = data.iloc[:, 4:]
    return population_stats.mean()


def max(data):
    population_stats = data.iloc[:, 4:]
    return population_stats.max()


def std(data):
    population_stats = data.iloc[:, 4:]
    return population_stats.std()


def summary(data):
    return data.info()


# plot Mean, Median, Standard Deviation of
# 5 years population growth% all over the world.
def countries_interest(data):
    result = data.loc[
        data["Country Name"].isin(["United States", "China", "India", "France"])
    ]
    return result


def viz_population(csv, jupyter=True):
    numeric_data = csv.iloc[:, 4:].apply(pd.to_numeric, errors="coerce")
    summary_stats = {
        "Mean": numeric_data.mean(),
        "Median": numeric_data.median(),
        "Std Dev": numeric_data.std(),
    }
    plt.figure(figsize=(8, 6))
    plt.plot(summary_stats["Mean"].index, summary_stats["Mean"].values, label="Mean")
    plt.plot(
        summary_stats["Median"].index, summary_stats["Median"].values, label="Median"
    )
    plt.plot(
        summary_stats["Std Dev"].index, summary_stats["Std Dev"].values, label="Std Dev"
    )
    plt.xlabel("Statistics")
    plt.ylabel("Values")
    plt.title("Summary Statistics")
    plt.legend()
    plt.tight_layout()
    plt.show()

    if jupyter:
        print("Visualization of Population Dataset")

    if not jupyter:
        print("Visualization of Population Dataset")


if __name__ == "__main__":
    data = pd.read_scv("/workspaces/Alicia_Individual_Project_1/src/population.csv")
    print("head: ", head(data))
    print("mean: ", mean(data))
    print("max: ", max(data))
    print("standard Deviation: ", std(data))
