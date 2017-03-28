# @brief Implementation of mastermind and mastermind solver in ruby
# @author P.E.Bontinck


# a class to handle combination
# == parameters:
# colors:: number of "colors", 6 by default
# slots:: number of slots, 4 by default
# uid:: serial number of the combination
# @todo unique add unique color in combination option
class Combination
  attr_reader :uid, :out, :colors, :slots
  
  def initialize arg, colors = 6, slots = 4
    @colors = colors
    if arg.class == 1234.class
      @uid = arg
      @slots = slots
      @out = Array.new(@slots).fill(0)
	  tab = @uid.digits(@colors)
      @out[0..(tab.size-1)] = tab
    else
      @out = arg
      @slots = arg.size
      @uid = 0
      @out.each_with_index {|i,j| @uid+=i*@colors**j}
    end
  end
  
  # @todo think should equal be the comparison operator returning
  # answer guesses ? in that case what is the purpose of uid ???
  def ==(c)
    # check first that color and slot number are comparable
	if (@colors != c.colors) or (@slots != c.slots)
	  raise "cannot compare combination from different game parameters"
	  return False
	end
	if @uid == c.uid # performance !
	  return true, @slots
	elsif @slots == 1 #in that case, the uids are not equal
	  return false, 0
	else
	  (1..@slots).each do |i|
	    if @out[i] == c.out[i]
          print "ok!"
	      # new to initialize with a tab
	    end
	  end
	end
  end
  
  def to_a
    @out
  end
  
  def [](i)
    @out[i]
  end
end

# A class to represent the game Master
# == Parameters
# comb:: serial number of the secret combination of the Master
class Master
  attr_accessor :comb
  
  def initialize comb
    @comb = comb
  end
  
  def answer(guess)
    recguess(guess, 0)
  end
  
  def recguess(guess, r)
    (0..(guess.to_a.size-1)).each do |i|
      if @comb[i] == guess[i]
        # @todo recursive_guess not sure the simple solution is to create combinations of smaller order
        return 1 + recguess(uid0.delete_at(i), uid1.delete(i))
      end
    end
  end
  
end

# algo : on liste toutes les combinaisons possibles ; puis on les
# supprime lorsque la réponse du master permet de les écarter.
