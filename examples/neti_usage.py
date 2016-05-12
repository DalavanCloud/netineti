from neti.neti_neti_trainer import NetiNetiTrainer
from src.neti_neti import NetiNeti

if __name__ == '__main__':
    print "Running NetiNeti Training, it might take a while..."

    nnt = NetiNetiTrainer()
    nn = NetiNeti(nnt)

    print nn.find_names("A frog-killing fungus known as Batrachochytrium dendrobatidis, or Bd, has already led to the decline of more than 200 amphibian species including the now extinct-in-the-wild Panamanian golden frog.")
