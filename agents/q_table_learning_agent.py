import numpy as np

class QTableLearningAgent(object):
    """QTableLearningAgent"""
    def __init__(self, env):
        self.action_space = env.action_space
        self.Q = np.zeros([env.observation_space.n, env.action_space.n])
        self.lr = .8
        self.y = .95
        self.num_episodes = 2000

    def act(self, observation, reward, done):
        action = np.argmax(Q[s, :] + np.random.randn(1,env.action_space.n)*(1./(i+1)))

    def learn(self, env):
        num_episodes = 2000
        rList = []
        for i in range(num_episodes):
          #Reset environment and get first new observation
            s = env.reset()
            rAll = 0
            d = False
            j = 0
            #The Q-Table learning algorithm
            while j < 99:
                j += 1
                #Choose an action by greedily (with noise) picking from Q table
                a = np.argmax(Q[s, :] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
                #Get new state and reward from environment
                s1,r,d,_ = env.step(a)
                #Update Q-Table with new knowledge
                Q[s,a] = Q[s,a] + lr * (r + y * np.max(Q[s1,:]) - Q[s,a])
                rAll += r
                s = s1
                if d == True:
                    break
            #jList.append(j)
            rList.append(rAll)

        return self.action_space.sample()
