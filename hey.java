

public class hey
{
    public static void main(String args[])
    {
        voiture mavoit = new voiture(9);
        voiture mavoit2 = new voiture(5);
        voiture mavoit3 = new voiture(4);
        voiture mavoit4 = new voiture(15);
        voiture.nbVoiture();
        
    }
}

class voiture
{
    public voiture(int nbroue)
    {
            this.nbroue = nbroue;
            System.out.println("Il y a " + nbroue + " roues");
            nbobj++;
    }

    public static void nbVoiture()
    {
        System.out.println("Il existe " + nbobj + " voitures");
    }

    private static int nbobj;
    private int nbroue;
}