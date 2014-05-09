// Copyright (c) 2013 Elements of Programming Interviews. All rights reserved.
// @author Ivan Sharov

package com.epi;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;

class Anagrams {
  // @include
  public static void findAnagrams(ArrayList<String> dictionary) {
    // Get the sorted string and then insert into hash table.
    HashMap<String, ArrayList<String>> hash = new HashMap<>();
    for (String s : dictionary) {
      char[] sortedCa = s.toCharArray();
      // Use sorted string as the hash code.
      Arrays.sort(sortedCa);
      String sortedStr = new String(sortedCa);
      if (!hash.containsKey(sortedStr)) {
        hash.put(sortedStr, new ArrayList<String>());
      }
      hash.get(sortedStr).add(s);
    }

    for (Map.Entry<String, ArrayList<String>> p : hash.entrySet()) {
      // Multiple strings with the same hash code => anagrams.
      if (p.getValue().size() >= 2) {
        // Output all strings.
        System.out.println(Arrays.toString(p.getValue().toArray()));
      }
    }
  }

  // @exclude

  private static String randString(int len) {
    StringBuilder ret = new StringBuilder();
    Random rnd = new Random();

    while (len-- > 0) {
      ret.append((char) (rnd.nextInt(26) + 97));
    }
    return ret.toString();
  }

  public static void main(String[] args) {
    Random rnd = new Random();
    ArrayList<String> dictionary = new ArrayList<String>();
    int n = rnd.nextInt(100000);
    HashSet<String> table = new HashSet<String>();
    for (int i = 0; i < n; ++i) {
      table.add(randString(rnd.nextInt(12) + 1));
    }
    for (String s : table) {
      dictionary.add(s);
    }
    findAnagrams(dictionary);
  }
}
