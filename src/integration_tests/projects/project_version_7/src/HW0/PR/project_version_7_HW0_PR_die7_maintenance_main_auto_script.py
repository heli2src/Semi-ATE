from ate_test_app.auto_script.AutoScriptBase import AutoScriptBase
from ate_common.logger import LogLevel

# logger and context are available, use as follow:
# self.logger
# self.context


class AutoScript(AutoScriptBase):
    def __init__(self):
        super().__init__()

    def after_cycle_teardown(self):
        pass

    def after_terminate_teardown(self):
        pass

    def after_exception_teardown(self, source: str, exception: Exception):
        pass