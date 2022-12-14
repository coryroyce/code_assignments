defmodule Identicon do
  @moduledoc """
  Project to take in a string input and generate an identicon
  """

  @doc """
  Main function for combining the smaller functions of the overall program

  ## Examples

      iex> Identicon.main("cory")

  """
  def main(input) do
    input
    |> hash_input
  end

  @doc """
  Create a hash based on MD5 from a string input

  ## Examples

      iex> Identicon.main("banana")
      [114, 179, 2, 191, 41, 122, 34, 138, 117, 115, 1, 35, 239, 239, 124, 65]

  """
  def hash_input(input) do
    :crypto.hash(:md5, input)
    |> :binary.bin_to_list
  end
end
