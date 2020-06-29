# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import time

from importlib import import_module

from .search import Search
from .process_arguments import ProcessArguments
from .verbosity import Verbosity


search_process_dict = {
    False: "SearchProcessNoMem",
    "short": "SearchProcessShortMem",
    "long": "SearchProcessLongMem",
}


class Optimizer:
    def __init__(
        self,
        random_state=None,
        verbosity=3,
        warnings=False,
        ext_warnings=False,
        hyperactive=False,
    ):
        self.verb = Verbosity(verbosity, warnings)
        self.random_state = random_state
        self.hyperactive = hyperactive
        self.search_processes = []

    def add_search(self, *args, **kwargs):
        pro_arg = ProcessArguments(args, kwargs, random_state=self.random_state)

        module = import_module(".search_process", "hyperactive")
        search_process_class = getattr(
            module, search_process_dict[pro_arg.kwargs["memory"]]
        )

        for nth_job in range(pro_arg.n_jobs):
            new_search_process = search_process_class(
                nth_job, pro_arg, self.verb, hyperactive=self.hyperactive
            )
            self.search_processes.append(new_search_process)

        self.search = Search(self.search_processes)

    def run(self, max_time=None):
        if max_time is not None:
            max_time = max_time * 60

        start_time = time.time()

        self.search.run(start_time, max_time)

        self.position_results = self.search.position_results
        self.eval_times = self.search.eval_times
        self.iter_times = self.search.iter_times
        # self.best_para = self.search.results
        # self.best_score = self.search.results

        """
        self.results = dist.results
        self.pos_list = dist.pos
        # self.para_list = None
        self.score_list = dist.scores

        self.eval_times = dist.eval_times
        self.iter_times = dist.iter_times
        self.best_scores = dist.best_scores
        """