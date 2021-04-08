from DummyTester.Testers.InterfaceSCT import InterfaceSCT


class MiniSCT(InterfaceSCT):
    def get_sites_count(self):
        return 1

    def do_request(self, site_id: int, timeout: int) -> bool:
        return True

    def test_in_progress(self, site_id: int):
        pass

    def test_done(self, site_id: int):
        pass

    def do_init_state(self, site_id: int):
        pass
