<h1 align="center">✨ Mr.PingPong-er ✨</h1>

<p align="center">
  <img src="./genetic screenshots/image.png" width="100" height="100" style="border-radius: 10px;">
</p>

<h4 align="center">An AI-Powered Ping Pong Game Featuring Neuroevolution</h4>
<hr>



> **Ping Pong Meets AI!**  
> In Mr.PingPong-er, a unique AI learns to play Ping Pong through generations of evolution using the NEAT algorithm. Experience the fascinating journey as the AI advances with each generation, gaining better skills to keep the ball in play. 🎾🤖

<p align="center">
  <img src="./genetic gifs/gen20.gif" height="400" width="600">
</p>

---

## 🚀 Project Overview

Mr.PingPong-er is a showcase of **AI evolution in games** using NEAT (Neuroevolution of Augmenting Topologies). Starting with a random population of 200 bars, the game evolves to enhance each bar's ability to prevent the ball from falling, refining its skills over successive generations. Through a crossover and mutation process, new "offspring" bars are created, learning better strategies to master the game with each iteration.



## 🔍 How It Works

### AI Technique: NEAT

NEAT is an evolutionary algorithm that optimizes neural networks, allowing each bar to learn and improve its gameplay over time. Here’s how it unfolds in Mr.PingPong-er:

1. **Generation Start:** 200 bars start with random movements, all aiming to prevent the ball from falling.
2. **Selection:** Bars that perform better become "parents" for the next generation.
3. **Crossover and Mutation:** The next generation is born by crossing over the parents' neural networks, with small mutations to encourage diversity.
4. **Repeat:** The cycle repeats, with each generation learning and improving.

<p align="center">
  <img src="./genetic screenshots/Straight.png" height="300" width="300">
</p>

### 🔍 Inputs & Vision

Each bar perceives its environment through five key “directions,” which help it assess its position and the ball’s movement. Here’s what each bar can "see":

<table>
  <tr>
    <th>Direction</th>
    <th>Description</th>
    <th>Image</th>
  </tr>
  <tr>
    <td><strong>Quadrant I</strong></td>
    <td>Distance to the ball in the upper-right quadrant.</td>
    <td><img src="./genetic screenshots/QI.png" alt="QI" width="100"></td>
  </tr>
  <tr>
    <td><strong>Quadrant II</strong></td>
    <td>Distance to the ball in the upper-left quadrant.</td>
    <td><img src="./genetic screenshots/QII.png" alt="QII" width="100"></td>
  </tr>
  <tr>
    <td><strong>Straight Overhead</strong></td>
    <td>Distance to the ball directly above.</td>
    <td><img src="./genetic screenshots/Straight.png" alt="Straight Overhead" width="100"></td>
  </tr>
  <tr>
    <td><strong>Left Wall Distance</strong></td>
    <td>Distance from the left wall.</td>
    <td><img src="./genetic screenshots/wall1.png" alt="Left Wall" width="100"></td>
  </tr>
  <tr>
    <td><strong>Right Wall Distance</strong></td>
    <td>Distance from the right wall.</td>
    <td><img src="./genetic screenshots/wall2.png" alt="Right Wall" width="100"></td>
  </tr>
</table>



## 🎯 Evolutionary Progress

### 🐣 Generation 1 - Initial Random Movements

In the first generation, bars make random movements, as they have no initial understanding of where or how to move.

<p align="center">
  <img src="./genetic gifs/gen2.gif" height="400" width="600">
</p>

### 🌱 Generation 6 - Developing Strategy

By Generation 6, bars begin to take sensible actions and are better at positioning themselves.

<p align="center">
  <img src="./genetic gifs/gen6.gif" height="400" width="600">
</p>

### 🚀 Generation 20+ - Mastery in Motion

As generations progress, the bars exhibit near-perfect decision-making and movement.

<p align="center">
  <img src="./genetic gifs/gen20.gif" height="400" width="600">
</p>



## 🛠 How to Run the Project

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/MrPingPong-er.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MrPingPong-er
   ```
3. Start the simulation:
   ```bash
   python pingpongAI.py
   ```



## 🌌 Future Scope

The current version of Mr.PingPong-er utilizes NEAT, but there’s room to experiment and innovate:

- **Deep Q-Learning:** Implementing a reinforcement learning approach, like Deep Q-Learning, could refine the AI’s decision-making abilities.
- **Hybrid Models:** Combining NEAT with reinforcement learning could yield even better gameplay.
- **Enhanced Mutation Rates:** Fine-tuning the mutation rates and crossover techniques might optimize performance.

Pull requests are welcome for any new ideas!



## 🤝 Contributing

Want to improve Mr.PingPong-er? Contributions are always welcome! Simply fork the repository, make your changes, and submit a pull request. Let’s make AI Ping Pong even smarter!

<p align="center">
  ⭐ Enjoy watching the AI evolve? Don’t forget to leave a star! ⭐
</p>
