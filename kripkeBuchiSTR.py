from Kernel import semanticTransitionRelations


class kripkeBuchiSTR(semanticTransitionRelations):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        return list(map(lambda rc: (None, rc), self.rhs.initial()))

    def actions(self, source):
        synchronons_actions = []
        kripke_src, buchi_src = source
        if kripke_src in None:
            for k_target in self.lhs.initial():
                self.get_synchronons_actions(k_target, buchi_src, synchronons_actions)
            return synchronons_actions
        k_actions = self.lhs.actions(kripke_src)
        num_actions = len(k_actions)
        for ka in k_actions:
            _, k_target = self.lhs.execute(kripke_src, ka)
            if k_target is None:
                num_actions -= 1
            self.get_synchronons_actions(k_target, buchi_src, synchronons_actions)

            if num_actions == 0:
                self.get_synchronons_actions(kripke_src, buchi_src, synchronons_actions)

    def get_synchronons_actions(self, kc, bc, io_synca):
        buchi_actions = self.rhs.actions(kc, bc)
        return io_synca.extend(map(lambda ba: (kc, ba), buchi_actions))

    def execute(self, action, conf):
        ktarget, baction = action
        _, bsrc = conf
        return ktarget, self.rhs.execute(ktarget, baction, bsrc)
