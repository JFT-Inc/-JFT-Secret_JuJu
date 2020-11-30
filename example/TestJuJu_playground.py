from jj.framework.secret_juju import juju
from jj.framework import juju_file_utility as fu

#program = juju()

if __name__ == "__main__":
    #program.loading methods
    #program.add component methods

    # program.start()

    repo = fu.jj_mini_repository("Example_1.txt")

    repo.setup_data_file()

    repo.pull()

    # repo.add_data("Hello?", "1234")
    # repo.add_data("Bye!", "4321")
    # repo.add_data("잘가?", "0987")
    # repo.add_data("안녕!", "6666")

    repo.add_data("Oh...!", "3333")

    repo.push()
