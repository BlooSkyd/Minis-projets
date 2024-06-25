#encoding: utf-8

def add(e1, e2):
    return e1+e2

def rem(e1, e2):
    return e1-e2

def mul(e1, e2):
    return e1*e2

def div(e1, e2):
    return e1/e2

def mod(e1, e2):
    return e1%e2

def eval(e):
    match e:
        case "test" :
            print()

# convertir les expressions en chaine de caractères ?
# avant de les parser
"""
type expr =
  | Const of int
  | Add of expr * expr
  | Sous of expr * expr
  | Neg of expr
  | Mul of expr * expr
  | Div of expr * expr
  | Res of expr * expr;;

let rec pp_expr e =
  match e with
  | Const i -> string_of_int i
  | Add (a,b) -> pp_expr a ^ "+" ^ pp_expr b
  | Sous (a,b) -> pp_expr a ^ "-" ^ pp_expr b
  | Neg i -> "-" ^ pp_expr i
  | Mul (a,b) -> pp_expr a ^ "*" ^ pp_expr b
  | Div (a,b) -> pp_expr a ^ "/" ^ pp_expr b
  | Res (a,b) -> pp_expr a ^ "%" ^ pp_expr b;;

let rec eval_expr e =
  match e with
  | Const i -> i
  | Add (a,b) -> eval_expr a + eval_expr b
  | Sous (a,b) -> eval_expr a - eval_expr b
  | Neg i -> - eval_expr i
  | Mul (a,b) -> (eval_expr a * eval_expr b)
  | Div (a,b) -> (eval_expr a / eval_expr b)
  | Res (a,b) -> (eval_expr a mod eval_expr b);;




"""


print("Fin du programme.")