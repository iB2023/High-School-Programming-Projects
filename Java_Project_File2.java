import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;

public class Calculator 
{
	JFrame window;  // the main window which contains everything
	Container content ;
	JButton[] digits = new JButton[12]; 
	JButton[] ops = new JButton[4];
	JTextField expression;
	JButton equals;
	JTextField result;
	private double TEMP;
	String display = "";
	
	public Calculator()
	{
		window = new JFrame( "Ivan's Calculator");
		content = window.getContentPane();
		content.setLayout(new GridLayout(2,1)); // 2 row, 1 col
		ButtonListener listener = new ButtonListener();
		
		// top panel holds expression field, equals sign and result field  
		// [4+3/2-(5/3.5)+3]  =   [3.456]
		
		JPanel topPanel = new JPanel();
		topPanel.setLayout(new GridLayout(1,3)); // 1 row, 3 col
		
		expression = new JTextField();
		expression.setFont(new Font("verdana", Font.BOLD, 16));
		expression.setText("");
		
		equals = new JButton("=");
		equals.setFont(new Font("verdana", Font.BOLD, 20 ));
		equals.addActionListener( listener ); 
		
		result = new JTextField();
		result.setFont(new Font("verdana", Font.BOLD, 16));
		result.setText("");
		
		topPanel.add(expression);
		topPanel.add(equals);
		topPanel.add(result);
						
		// bottom panel holds the digit buttons in the left sub panel and the operators in the right sub panel
		JPanel bottomPanel = new JPanel();
		bottomPanel.setLayout(new GridLayout(1,2)); // 1 row, 2 col
	
		JPanel  digitsPanel = new JPanel();
		digitsPanel.setLayout(new GridLayout(4,3));	
		
		for (int i=0 ; i<10 ; i++ )
		{
			digits[i] = new JButton( ""+i );
			digitsPanel.add( digits[i] );
			digits[i].addActionListener( listener ); 
		}
		digits[10] = new JButton( "C" );
		digitsPanel.add( digits[10] );
		digits[10].addActionListener( listener ); 

		digits[11] = new JButton( "CE" );
		digitsPanel.add( digits[11] );
		digits[11].addActionListener( listener ); 		
	
		JPanel opsPanel = new JPanel();
		opsPanel.setLayout(new GridLayout(4,1));
		String[] opCodes = { "+", "-", "*", "/" };
		for (int i=0 ; i<4 ; i++ )
		{
			ops[i] = new JButton( opCodes[i] );
			opsPanel.add( ops[i] );
			ops[i].addActionListener( listener ); 
		}
		bottomPanel.add( digitsPanel );
		bottomPanel.add( opsPanel );
		
		content.add( topPanel );
		content.add( bottomPanel );
	
		window.setSize( 640,480);
		window.setVisible( true );
	}



	class ButtonListener implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			Component whichButton = (Component) e.getSource();
			
			for (int i=0 ; i<10 ; i++ )
				if (whichButton == digits[i])
					expression.setText( expression.getText() + i );
					
				
			if (whichButton == digits[10])
				expression.setText("");

			if ( whichButton == digits[11])
				expression.setText(expression.getText().substring(0, expression.getText().length()-1));
      
			if (whichButton == ops[0])
				expression.setText(expression.getText() + "+" );
			else if (whichButton == ops[1])
				expression.setText(expression.getText() + "-");
			else if (whichButton == ops[2])
				expression.setText(expression.getText() + "*");
			else if (whichButton == ops[3])
				expression.setText(expression.getText() + "/");

			if(whichButton == equals)
			{
				String expr=expression.getText();
				ArrayList<String> operators = new ArrayList<String>();
				ArrayList<String> operands = new ArrayList<String>();
				StringTokenizer sT = new StringTokenizer(expr,"+-*/", true );
				while (sT.hasMoreTokens())
				{
					String token = sT.nextToken();
					if ("+-*/".contains(token))
						operators.add(token);
					else
						operands.add(token);
				}
				System.out.println(operands+"\n"+operators);

				if(operands.size()== operators.size()  || (operators.size() - operands.size())>1)

					result.setText("INVALID EXPRESSION");
				while ( (operators.contains("*")) || (operators.contains("/")))
				{
					int i = operators.indexOf("*");
					int j = operators.indexOf("/");

					if (i>=0 && (i>j || j == -1))
					{
						double first = Double.parseDouble(operands.get(i));

						double second = Double.parseDouble(operands.get(i+1));

						double newValue = (first * second);
						operands.set(i, newValue+""); 
						operands.remove(i+1);
						operators.remove(i);
					}
          
					if (j>=0 && (j>i || i == -1))
					{
						double first = Double.parseDouble(operands.get(j));

						double second = Double.parseDouble(operands.get(j+1));

						double newValue = (first / second);
						operands.set(j, newValue+""); 
						operands.remove(j+1);
						operators.remove(j);
					}
				}
				while ( (operators.contains("+")) || (operators.contains("-")))
				{
					int i = operators.indexOf("+");
					int j = operators.indexOf("-");

					if (i>=0 && (i>j || j == -1))
					{
						double first = Double.parseDouble(operands.get(i));

						double second = Double.parseDouble(operands.get(i+1));

						double newValue = (first + second);
						operands.set(i, newValue+""); 
						operands.remove(i+1);
						operators.remove(i);
					}
          
					if (j>=0 && (j>i || i == -1))
					{
						double first = Double.parseDouble(operands.get(j));

						double second = Double.parseDouble(operands.get(j+1));

						double newValue = (first - second);
						operands.set(j, newValue+""); 
						operands.remove(j+1);
						operators.remove(j);
					}
				}
					result.setText(operands.get(0));
			}
		}
	}
  
	public static void main(String [] args)
	{

		new Calculator();
	}
  
}
