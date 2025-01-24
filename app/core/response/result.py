class ResultAPI:

    def __init__(
        self,
        error: bool = False,
        code: str = None,
        code_list: list[tuple[bool, str]] = None,
    ):
        self.error = error

        if code_list:
            for tuple in code_list:
                self.code, self.error = tuple

                if self.error:
                    break

        if code is not None:
            self.code = code
            self.error = error
