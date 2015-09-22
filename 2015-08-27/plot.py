import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def speedup(p, alpha):
  return 1. / (alpha + ((1. - alpha) / p))

def efficieny(p, alpha):
  return speedup(p, alpha) / p



def main():
  alpha = 0.1
  x_pts = range(1,129)
  speed = [speedup(p, alpha) for p in x_pts]
  eff = [efficieny(p, alpha) for p in x_pts]

  plt.plot(x_pts,speed)
  plt.xlabel('Num Processors')
  plt.ylabel('Speedup')
  plt.savefig('speedup.pdf')

  plt.figure()
  plt.plot(x_pts, eff)
  plt.xlabel('Number of Processors')
  plt.ylabel('Efficiency')
  plt.savefig('eff.pdf')


if __name__ == "__main__":
    main()
   
