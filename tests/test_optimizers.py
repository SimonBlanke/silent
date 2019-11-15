# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from hyperactive import Hyperactive

data = load_iris()
X = data.data
y = data.target

n_iter = 30


def model(para, X_train, y_train):
    model = DecisionTreeClassifier(
        criterion=para["criterion"],
        max_depth=para["max_depth"],
        min_samples_split=para["min_samples_split"],
        min_samples_leaf=para["min_samples_leaf"],
    )
    scores = cross_val_score(model, X_train, y_train, cv=2)

    return scores.mean()


search_config = {
    model: {
        "criterion": ["gini", "entropy"],
        "max_depth": range(1, 11),
        "min_samples_split": range(2, 11),
        "min_samples_leaf": range(1, 11),
    }
}


def test_HillClimbingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="HillClimbing")
    opt.search(search_config)


def test_StochasticHillClimbingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="StochasticHillClimbing")
    opt.search(search_config)


def test_TabuOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="TabuSearch")
    opt.search(search_config)


def test_RandomSearchOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="RandomSearch")
    opt.search(search_config)


def test_RandomRestartHillClimbingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="RandomRestartHillClimbing")
    opt.search(search_config)


def test_RandomAnnealingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="RandomAnnealing")
    opt.search(search_config)


def test_SimulatedAnnealingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="SimulatedAnnealing")
    opt.search(search_config)


def test_StochasticTunnelingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="StochasticTunneling")
    opt.search(search_config)


def test_ParallelTemperingOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="ParallelTempering")
    opt.search(search_config)


def test_ParticleSwarmOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="ParticleSwarm")
    opt.search(search_config)


def test_EvolutionStrategyOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="EvolutionStrategy")
    opt.search(search_config)


def test_BayesianOptimizer():
    opt = Hyperactive(X, y, n_iter=n_iter, optimizer="Bayesian")
    opt.search(search_config)
