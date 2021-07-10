# snake-AI-


Basic Working :
  1. Created snakes game using pygame which acts as the environment
  2. The deep -Q - Learning Algo consists of a neural network created using pytorch which acts as our model
  3. Created an agent that trains the AI
  
  General flow:
  Agent:
    Game
    Model
    Training:
      state=get_state(game)
      action=model.predict(state)
      reward,game_over,score=game.play_step(action)
      new_state=get_state(game)
      remember(state,action,new_state,reward,game_over)
      model.train()
      
      
      
  Reward:
    +10 for food
    -10 for collision
    0 other wise
  
  Action:
    [1,0,0] move straight
    [0,1,0] go left
    [0,0,1] go right
    
  State:
  [Danger straight,Danger Right,Danger Left,
  
   Direction Left,  Direction Right,  Direction Up,  Direction Down,
   
   Food Left, Food Right, Food Up, Food Down
  ]
  
  Model:
    1 input layer of size 11
    1 Hidden layer of size 256(can play with this)
    1 output layer of size 3
    using pytorch

https://user-images.githubusercontent.com/37270043/125150179-7e2bb800-e15b-11eb-8bdf-889cf5d1bfbd.mov
