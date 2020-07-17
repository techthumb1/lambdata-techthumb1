{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "High Kick High Snare Low Bass\n",
      "I AM PLAYING THE High Snare\n",
      "PLAYING THE SOUNDFONT\n",
      "I AM PLAYING THE Mid Snare WITH Deep Bass\n",
      "PLAYING THE SOUNDFONT\n"
     ]
    }
   ],
   "source": [
    "# beat.py\n",
    "\n",
    "class Beat():\n",
    "    def __init__(self, kick, snare, hat, bass):\n",
    "        self.kick = kick\n",
    "        self.snare = snare\n",
    "        self.hat = hat\n",
    "        self.bass = bass\n",
    "\n",
    "    def instrument(self):\n",
    "        print(\"PLAYING THE SOUNDFONT\")\n",
    "\n",
    "    def keys(self):\n",
    "        print(\"I AM PLAYING THE\", self.snare)\n",
    "\n",
    "\n",
    "class Hip_Hop(Beat):\n",
    "    def __init__(self, kick, snare, hat, bass, trap_bass):\n",
    "        super().__init__(kick, snare, hat, bass)\n",
    "        self.trap_bass = trap_bass\n",
    "\n",
    "    def keys(self):\n",
    "        print(\"I AM PLAYING THE\", self.snare, \"WITH\", self.trap_bass)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    soundfont = Beat(\"High Kick\", \"High Snare\", \"High Hat\", \"Low Bass\")\n",
    "    print(soundfont.kick, soundfont.snare, soundfont.bass)\n",
    "    soundfont.keys()\n",
    "    soundfont.instrument()\n",
    "\n",
    "    keys = Hip_Hop(\"Low Kick\", \"Mid Snare\", \"Low Hat\", \"Mid Bass\", \"Deep Bass\")\n",
    "    keys.keys()\n",
    "    keys.instrument()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Functional Approach"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'compat'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-63810204753b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;31m# FUNCTIONAL APPROACH\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m# State abbreviation -> Full Name and visa versa.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    190\u001b[0m \u001b[1;31m# GH 27101\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    191\u001b[0m \u001b[1;31m# TODO: remove Panel compat in 1.0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 192\u001b[1;33m \u001b[1;32mif\u001b[0m \u001b[0mpandas\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcompat\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPY37\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    193\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    194\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'compat'"
     ]
    }
   ],
   "source": [
    "# my_lambdata/assignment.py\n",
    "# FUNCTIONAL APPROACH\n",
    "\n",
    "import pandas\n",
    "\n",
    "# State abbreviation -> Full Name and visa versa.\n",
    "# FL -> Florida, etc.\n",
    "# (Handle Washington DC and territories like Puerto Rico etc.)\n",
    "\n",
    "def add_state_names(my_df):\n",
    "    \"\"\" Param my_df pandas dataframe with column name \"abbrevs\" \"\"\"\n",
    "    new_df = my_df.copy() # don't mutate existing df (just a pref, you could mutate and not return anything if you want)\n",
    "    names_map = {\n",
    "        \"CA\": \"Cali\",\n",
    "        \"CO\": \"Colo\",\n",
    "        \"CT\": \"Conn\",\n",
    "        \"DC\": \"Wash DC\",\n",
    "        \"TX\": \"Texas\"\n",
    "    }\n",
    "    #breakpoint()\n",
    "    my_col = new_df[\"abbrevs\"]\n",
    "    other_col = my_col.map(names_map)\n",
    "    new_df[\"state_name\"] = other_col\n",
    "    return new_df\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    #print(\"hahahah\")\n",
    "    #input(\".............\")\n",
    "\n",
    "    df = pandas.DataFrame({\"abbrevs\": [\"CA\", \"CO\", \"CT\", \"DC\", \"TX\"]})\n",
    "    print(type(df))\n",
    "    print(df.head())\n",
    "\n",
    "    df2 = add_state_names(df)\n",
    "    print(df2.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## OOP Approach"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# my_lambdata/assignment.py\n",
    "# OOP APPROACH\n",
    "\n",
    "import pandas\n",
    "\n",
    "class DataFrameTransformer(object):\n",
    "    def __init__(self, df):\n",
    "        \"\"\"Param df pandas dataframe with column name \"abbrevs\" \"\"\"\n",
    "        self.df = df\n",
    "\n",
    "    def inspect_data(self):\n",
    "        print(self.df.head())\n",
    "\n",
    "    def add_state_names(self):\n",
    "        \"\"\"\n",
    "        State abbreviation -> Full Name and visa versa.\n",
    "        FL -> Florida, etc.\n",
    "        \"\"\"\n",
    "        names_map = {\n",
    "            \"CA\": \"Cali\",\n",
    "            \"CO\": \"Colo\",\n",
    "            \"CT\": \"Conn\",\n",
    "            \"DC\": \"Wash DC\",\n",
    "            \"TX\": \"Texas\"\n",
    "        }\n",
    "        #breakpoint()\n",
    "        my_col = self.df[\"abbrevs\"]\n",
    "        other_col = my_col.map(names_map)\n",
    "        self.df[\"state_name\"] = other_col\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    df = pandas.DataFrame({\"abbrevs\": [\"CA\", \"CO\", \"CT\", \"DC\", \"TX\"]})\n",
    "\n",
    "    transformer = DataFrameTransformer(df)\n",
    "    transformer.inspect_data()\n",
    "\n",
    "    transformer.add_state_names()\n",
    "    transformer.inspect_data()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Inheritance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# my_lambdata/assignment_w_inherit.py\n",
    "# Inheritance\n",
    "\n",
    "import pandas\n",
    "\n",
    "class MyFrame(pandas.DataFrame):\n",
    "\n",
    "    def inspect_data(self):\n",
    "        print(self.head())\n",
    "\n",
    "    def add_state_names(self):\n",
    "        \"\"\"\n",
    "        State abbreviation -> Full Name and visa versa.\n",
    "        FL -> Florida, etc.\n",
    "        \"\"\"\n",
    "        names_map = {\n",
    "            \"CA\": \"Cali\",\n",
    "            \"CO\": \"Colo\",\n",
    "            \"CT\": \"Conn\",\n",
    "            \"DC\": \"Wash DC\",\n",
    "            \"TX\": \"Texas\"\n",
    "        }\n",
    "        #breakpoint()\n",
    "        my_col = self[\"abbrevs\"]\n",
    "        other_col = my_col.map(names_map)\n",
    "        self[\"state_name\"] = other_col\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    #df = pandas.DataFrame({\"abbrevs\": [\"CA\", \"CO\", \"CT\", \"DC\", \"TX\"]})\n",
    "\n",
    "    my_frame = MyFrame({\"abbrevs\": [\"CA\", \"CO\", \"CT\", \"DC\", \"TX\"]})\n",
    "    print(my_frame.head())\n",
    "    my_frame.inspect_data()\n",
    "    my_frame.add_state_names()\n",
    "    my_frame.inspect_data()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Unittest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "'pipimport' is not recognized as an internal or external command,\n",
      "operable program or batch file.\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "module 'pandas' has no attribute 'compat'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-d87c8b2962bc>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'pipimport unittest'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mDataFrame\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mmy_lambdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0massignment\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0madd_state_names\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    190\u001b[0m \u001b[1;31m# GH 27101\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    191\u001b[0m \u001b[1;31m# TODO: remove Panel compat in 1.0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 192\u001b[1;33m \u001b[1;32mif\u001b[0m \u001b[0mpandas\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcompat\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPY37\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    193\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    194\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'pandas' has no attribute 'compat'"
     ]
    }
   ],
   "source": [
    "!pipimport unittest\n",
    "from pandas import DataFrame\n",
    "from my_lambdata.assignment import add_state_names\n",
    "# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file\n",
    "\n",
    "class TestAssignment(unittest.TestCase):\n",
    "    def test_add_state_names(self):\n",
    "        # expect that it has one more column and the same number of rows, after we invoke the function\n",
    "        # expect that certain column names exist before and certain col names exist after\n",
    "        df = DataFrame({\"abbrev\":[\"CA\",\"CO\",\"CT\",\"DC\",\"TX\"]})\n",
    "        self.assertEqual(list(df.columns), ['abbrev'])\n",
    "        result = add_state_names(df)\n",
    "        self.assertEqual(list(result.columns), [\"abbrev\", \"name\"])\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
