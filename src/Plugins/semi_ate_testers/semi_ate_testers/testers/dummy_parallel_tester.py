from semi_ate_testers.testers.tester_interface import TesterInterface

class DummyParallelTester(TesterInterface):
    def get_sites_count(self):
        # TODO: temporary value for 16
        return 16

    def do_request(self, site_id: int, timeout: int) -> bool:
        return True

    def test_in_progress(self, site_id: int):
        pass

    def test_done(self, site_id: int, timeout: int):
        pass

    def do_init_state(self, site_id: int):
        pass