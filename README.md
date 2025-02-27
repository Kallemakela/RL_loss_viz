# Visualizing RL Loss Functions

## PPO loss

loss = -min(ratio * A, clip(ratio, 1 - e, 1 + e) * A)

ratio = pi(a) / pi_old(a)

e = 0.1

### A=1
<table id="T_dd513">
  <thead>
    <tr>
      <th class="index_name level0" >pi(a)</th>
      <th id="T_dd513_level0_col0" class="col_heading level0 col0" >0.1</th>
      <th id="T_dd513_level0_col1" class="col_heading level0 col1" >0.5</th>
      <th id="T_dd513_level0_col2" class="col_heading level0 col2" >0.9</th>
    </tr>
    <tr>
      <th class="index_name level0" >pi_old(a)</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_dd513_level0_row0" class="row_heading level0 row0" >0.1</th>
      <td id="T_dd513_row0_col0" style="background-color: #199750;
  color: #f1f1f1;" class="data row0 col0" >-1.00</td>
      <td id="T_dd513_row0_col1" style="background-color: #006837;
  color: #f1f1f1;" class="data row0 col1" >-1.10</td>
      <td id="T_dd513_row0_col2" style="background-color: #006837;
  color: #f1f1f1;" class="data row0 col2" >-1.10</td>
    </tr>
    <tr>
      <th id="T_dd513_level0_row1" class="row_heading level0 row1" >0.5</th>
      <td id="T_dd513_row1_col0" style="background-color: #d22b27;
  color: #f1f1f1;" class="data row1 col0" >-0.20</td>
      <td id="T_dd513_row1_col1" style="background-color: #199750;
  color: #f1f1f1;" class="data row1 col1" >-1.00</td>
      <td id="T_dd513_row1_col2" style="background-color: #006837;
  color: #f1f1f1;" class="data row1 col2" >-1.10</td>
    </tr>
    <tr>
      <th id="T_dd513_level0_row2" class="row_heading level0 row2" >0.9</th>
      <td id="T_dd513_row2_col0" style="background-color: #a50026;
  color: #f1f1f1;" class="data row2 col0" >-0.11</td>
      <td id="T_dd513_row2_col1" style="background-color: #fff0a6;
  color: #000000;" class="data row2 col1" >-0.56</td>
      <td id="T_dd513_row2_col2" style="background-color: #199750;
  color: #f1f1f1;" class="data row2 col2" >-1.00</td>
    </tr>
  </tbody>
</table>

### A=-1
<table id="T_4af0d">
  <thead>
    <tr>
      <th class="index_name level0" >pi(a)</th>
      <th id="T_4af0d_level0_col0" class="col_heading level0 col0" >0.1</th>
      <th id="T_4af0d_level0_col1" class="col_heading level0 col1" >0.5</th>
      <th id="T_4af0d_level0_col2" class="col_heading level0 col2" >0.9</th>
    </tr>
    <tr>
      <th class="index_name level0" >pi_old(a)</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_4af0d_level0_row0" class="row_heading level0 row0" >0.1</th>
      <td id="T_4af0d_row0_col0" style="background-color: #036e3a;
  color: #f1f1f1;" class="data row0 col0" >1.00</td>
      <td id="T_4af0d_row0_col1" style="background-color: #fffdbc;
  color: #000000;" class="data row0 col1" >5.00</td>
      <td id="T_4af0d_row0_col2" style="background-color: #a50026;
  color: #f1f1f1;" class="data row0 col2" >9.00</td>
    </tr>
    <tr>
      <th id="T_4af0d_level0_row1" class="row_heading level0 row1" >0.5</th>
      <td id="T_4af0d_row1_col0" style="background-color: #006837;
  color: #f1f1f1;" class="data row1 col0" >0.90</td>
      <td id="T_4af0d_row1_col1" style="background-color: #036e3a;
  color: #f1f1f1;" class="data row1 col1" >1.00</td>
      <td id="T_4af0d_row1_col2" style="background-color: #219c52;
  color: #f1f1f1;" class="data row1 col2" >1.80</td>
    </tr>
    <tr>
      <th id="T_4af0d_level0_row2" class="row_heading level0 row2" >0.9</th>
      <td id="T_4af0d_row2_col0" style="background-color: #006837;
  color: #f1f1f1;" class="data row2 col0" >0.90</td>
      <td id="T_4af0d_row2_col1" style="background-color: #006837;
  color: #f1f1f1;" class="data row2 col1" >0.90</td>
      <td id="T_4af0d_row2_col2" style="background-color: #036e3a;
  color: #f1f1f1;" class="data row2 col2" >1.00</td>
    </tr>
  </tbody>
</table>

## REINFORCE loss

loss = -log(pi(a)) * A

<table id="T_c349e">
  <thead>
    <tr>
      <th class="index_name level0" >pi(a)</th>
      <th id="T_c349e_level0_col0" class="col_heading level0 col0" >0.01</th>
      <th id="T_c349e_level0_col1" class="col_heading level0 col1" >0.5</th>
      <th id="T_c349e_level0_col2" class="col_heading level0 col2" >0.99</th>
    </tr>
    <tr>
      <th class="index_name level0" >A</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c349e_level0_row0" class="row_heading level0 row0" >-1.0</th>
      <td id="T_c349e_row0_col0" style="background-color: #006837;
  color: #f1f1f1;
  text-align: right;" class="data row0 col0" >-4.61</td>
      <td id="T_c349e_row0_col1" style="background-color: #e2f397;
  color: #000000;
  text-align: right;" class="data row0 col1" >-0.69</td>
      <td id="T_c349e_row0_col2" style="background-color: #feffbe;
  color: #000000;
  text-align: right;" class="data row0 col2" >-0.01</td>
    </tr>
    <tr>
      <th id="T_c349e_level0_row1" class="row_heading level0 row1" >1.0</th>
      <td id="T_c349e_row1_col0" style="background-color: #a50026;
  color: #f1f1f1;
  text-align: right;" class="data row1 col0" >4.61</td>
      <td id="T_c349e_row1_col1" style="background-color: #fee797;
  color: #000000;
  text-align: right;" class="data row1 col1" >0.69</td>
      <td id="T_c349e_row1_col2" style="background-color: #fffebe;
  color: #000000;
  text-align: right;" class="data row1 col2" >0.01</td>
    </tr>
  </tbody>
</table>