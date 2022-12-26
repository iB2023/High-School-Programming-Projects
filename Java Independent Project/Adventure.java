//TODO: 1. 
import java.util.Scanner;
import java.util.Random;
public class Adventure {
	
	public static void main(String[] args)
	{
		Random randomGenerator = new Random ();
		// Initialize player name and level
int playerLevel = 1;
String playerName = "Ivan";
double playerHealth = 10.0;	
Scanner userInput = new Scanner(System.in);
System.out.println("What is your character's name?");
playerName = userInput.nextLine();	
//TODO: 2. Scanner userInput = new Scanner(System.in);
//TODO: 3. Print a message asking the player to enter their character's name
//TODO: 4. Use your scanner to read the user's input 
System.out.println("Welcome " + playerName + "!"); 
System.out.println("Before you is an enormous cave mouth. Darkness is before you, but adventure awaits. Dare you enter the Cave of Wonders?");
System.out.println("1. Enter the Cave of Wonders");
System.out.println("2. Run away to the safety of your warm bed");
int playerChoice;
playerChoice = userInput.nextInt();
if(playerChoice == 1) {
	// The player enters the cave
	System.out.println("You made it to the entrance of the cave.");
    playerLevel++;
    System.out.println("Your bravery has rewarded you! Congratulations, you are now level " + playerLevel);
    
    // Trap is triggered
    System.out.println("You travel forward into the dark cave. You feel something press against your leg...");
    System.out.println("It's a trap! Suddenly, you're being bombarded by rocks from above.");
    int rockDamage;
    rockDamage = randomGenerator.nextInt(5);
    playerHealth -= rockDamage;
    System.out.println("The rock slide hits you for " + rockDamage + "!");
    System.out.println("You have " + playerHealth + " health remaining.");
    
 // The player finds a chest
    System.out.println("You pick yourself up from the cave floor and brush a cloud of dust from your clothes.");
    System.out.println("The cave narrows as you press on until you manage to squeeze through a tiny opening into a large natural cavern.");
    System.out.println("Before you is a glorious treasure chest.");
     //TODO: 1. Declare a boolean to represent if the player has the sword.
     //TODO: 2. Ask your player if they would like to open the chest.
     //TODO: 3. Use your scanner to read the player's choice.
    boolean hasSword = false;
    System.out.println("1. Open the chest.");
    System.out.println("2. Ignore the chest. Obvious trap is obvious.");
    playerChoice = userInput.nextInt();
    
    if(playerChoice == 1){
        System.out.println("Uneasy after your brush with death, you slowly open the chest to reveal a shiny, magical,diamond sword!");
        hasSword = true;
    }
    
    System.out.println("You leave the cavern with the chest and continue your journey");
    System.out.println("Up ahead the air grows warm and wet. You hear snoring.");
    System.out.println("Peeking around a corner you see a monstrous shape! A dragon sleeps in the room ahead.");
    System.out.println("You swallow hard and decide it is time to leave.");
    System.out.println("As you turn your foot finds a rock. It thuds loudly against the cave wall. The dragon wakes up!");
    System.out.println("1. Fight the Dragon.");
    System.out.println("2. Run for your life.");
    playerChoice = userInput.nextInt();
    if(playerChoice == 1){
      // The player fights the dragon
        System.out.println("You feel courage surge through your body as you charge the dragon with your sword!");
        if(hasSword){
            System.out.println("You raise the magic sword and plunge it into the dragon slaying the beast.");
        }else {
            System.out.println("You pummel the dragon with your fists to no avail. The dragon snarls and swallows you whole. Game Over!");
            System.exit(0);
        }
    }else {
      // The player flees
        System.out.println("As you run away to hide in the safety of your warm bed, the dragon yawns and returns to its slumber.");
    }
    
} else {
	// The player runs away }
	  System.out.println(playerName + " runs home and goes to sleep.");
      System.exit(0);
}

}
}