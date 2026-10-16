import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Get user input from console --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# -------- Agent Definition -----------
class RandomWalker(ap.Agent):
    def step(self):
        direction = random.choices([(1, 0), (-1, 0), (0, 1), (0, -1)], weights=[3, 1, 1, 1], k=1)[0]
        x, y = self.position
        # Keep agents inside grid
        x = max(0, min(self.model.p.grid_size[0]-1, x + direction[0]))
        y = max(0, min(self.model.p.grid_size[1]-1, y + direction[1]))
        self.position = (x, y)
        self.path.append(self.position)

# -------- Model Definition -----------
class RandomWalkModel(ap.Model):
    def setup(self):
        # Create agents
        self.agents = ap.AgentList(self, self.p.agents, RandomWalker)

        # Initialize random positions
        for agent in self.agents:
            agent.position = (random.randint(0, self.p.grid_size[0]-1),
                              random.randint(0, self.p.grid_size[1]-1))
            agent.path = [agent.position] 

        # Create grid (optional)
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.grid.add_agents(self.agents)

    def step(self):
        for agent in self.agents:
            agent.step()

# -------- Parameters from user input -----------
parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps
}

# -------- Run Model -----------
model = RandomWalkModel(parameters)
model.setup()

# -------- Interactive Animation -----------
fig, ax = plt.subplots()
ax.set_xlim(0, model.p.grid_size[0])
ax.set_ylim(0, model.p.grid_size[1])
ax.set_xticks(range(model.p.grid_size[0]+1))
ax.set_yticks(range(model.p.grid_size[1]+1))
ax.grid(True)

scat = ax.scatter([], [], s=200)

path_lines = [ax.plot([], [], linewidth=1.5, label=f"Agent {i}")[0]
              for i in range(1, num_agents + 1)]

def init():
    positions = [agent.position for agent in model.agents]
    scat.set_offsets(positions)
    return scat,

def update(frame):
    model.step()
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]
    scat.set_offsets(list(zip(x, y)))
    for agent, line in zip(model.agents, path_lines):
        path_x = [position[0] for position in agent.path]
        path_y = [position[1] for position in agent.path]
        line.set_data(path_x, path_y)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=model.p.steps, init_func=init, blit=False, repeat=False)
ax.legend()
plt.show()

for number, agent in enumerate(model.agents, start=1):
    print(f"Agent {number} path: {agent.path}")

from collections import Counter

final_positions = [agent.position for agent in model.agents]
position_counts = Counter(final_positions)

print("\nFinal position distribution:")
for position, count in sorted(position_counts.items()):
    print(f"{position}: {count} agent(s)")

average_x = sum(x for x, y in final_positions) / len(final_positions)
print(f"Average final x-position: {average_x:.2f}")
