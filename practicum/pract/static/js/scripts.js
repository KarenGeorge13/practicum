function Popup()
{
    button = document.getElementById('savebutton');
    form = document.querySelector('#blablabla');
    popup = document.querySelector('.popup');
    form.classList.add('open');
    popup.classList.add('popup_open');
}
function Cancel()
{
    button = document.getElementById('cancelbutton');
    form = document.querySelector('#blablabla');
    popup = document.querySelector('.popup');
    form.classList.remove('open');
    popup.classList.remove('popup_open');
}
function loadFunc()
{
    Selected();
    Changed(false);
    Scroll();
}
function Selected()
{
    if(document.getElementById("id_pulse_0").checked == true)
    {
        document.getElementById("id_ccf").value = 0;
        document.getElementById("id_ccf").readOnly = true;
        document.getElementById("id_mcf").value = 1;
        document.getElementById("id_mcf").readOnly = true;
    }
    if(document.getElementById("id_pulse_1").checked == true)
    {
        document.getElementById("id_ccf").readOnly = false;
        document.getElementById("id_mcf").readOnly = false;
    }
    if(document.getElementById("id_pulse_2").checked == true)
    {
        document.getElementById("id_ccf").readOnly = false;
        document.getElementById("id_mcf").value = 1;
        document.getElementById("id_mcf").readOnly = true;
    }
}
function Changed(isChange)
{
    if(isChange == true)
    {
        Clear();
    }
    var val = document.getElementById("id_norm_length").value;
    if(val == "L_cp")
    {
        document.getElementById("id_L").value = 1;
        document.getElementById("id_L").readOnly = true;
    }
    if(val == "L_D2")
    {
        document.getElementById("id_muFD2").value = 1;
        document.getElementById("id_muFD2").readOnly = true;
    }
    if(val == "L_D3")
    {
        document.getElementById("id_muFD3").value = 1;
        document.getElementById("id_muFD3").readOnly = true;
    }
    if(val == "L_NL")
    {
        document.getElementById("id_muFN").value = 1;
        document.getElementById("id_muFN").readOnly = true;
    }
    if(val == "L_S")
    {
        document.getElementById("id_muFs").value = 1;
        document.getElementById("id_muFs").readOnly = true;
    }
    if(val == "L_ICS")
    {
        document.getElementById("id_muFL").value = 1;
        document.getElementById("id_muFL").readOnly = true;
    }
}
function Clear()
{
    document.getElementById("id_L").readOnly = false;

    document.getElementById("id_muFD2").readOnly = false;

    document.getElementById("id_muFD3").readOnly = false;

    document.getElementById("id_muFN").readOnly = false;

    document.getElementById("id_muFs").readOnly = false;

    document.getElementById("id_muFL").readOnly = false;
}
function Reset()
{
    document.getElementById("id_T").value = 40;
    document.getElementById("id_N").value = 1024;
    document.getElementById("id_norm_length").value = "Lcp";
    document.getElementById("id_L").value = 1;
    document.getElementById("id_N1").value = 2000;

    document.getElementById("id_muFD2").value = 0;
    document.getElementById("id_sgn2").value = 1;
    document.getElementById("id_muFD3").value = 0;
    document.getElementById("id_sgn3").value = 1;
    document.getElementById("id_muFN").value = 0;
    document.getElementById("id_muFs").value = 0;
    document.getElementById("id_muFL").value = 0;
    document.getElementById("id_alpha0").value = 0;

    document.getElementById("id_impulse_0").checked = true;
    document.getElementById("id_ccf").value = 0;
    document.getElementById("id_mcf").value = 1;
}
function Scroll()
{
    document.getElementById("top-chart").scrollIntoView(true);
}
function Alert()
{
    alert("Войдите, чтобы сохранять парметры");
}