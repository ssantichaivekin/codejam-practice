import java.io.*;
import java.util.*;
import java.math.*;

public class ProblemB {
	int gcd(int A, int B) {
		while (A>0&&B>0)
			if (A>B) A%=B; else B%=A;
		return A+B;
	}
	
	boolean share(int A, int B, int P) {
		int x = gcd(A, B);
		for (int i=2; i<P;i++)
			while (x%i==0) x/=i;
		return (x>1);
	}
	
	void doMain() throws Exception {
		Scanner sc = new Scanner(new FileReader("input.txt"));
		PrintWriter pw = new PrintWriter(new FileWriter("output.txt"));
		int caseCnt = sc.nextInt();
		for (int caseNum=1; caseNum <= caseCnt; caseNum++) {
			pw.print("Case #" + caseNum + ": ");
			int A = sc.nextInt();
			int B = sc.nextInt();
			int P = sc.nextInt();
			int[] id = new int[1001];
			int res = 0;
			for (int i=A; i<=B; i++) {
				id[i] = i;
				res++;
			}
			for (int i=A; i<=B; i++)
				for (int j=i+1; j<=B; j++)
					if (id[i]!=id[j] && share(i, j, P)) {
						int idi = id[i], idj=id[j];
						res--;
						for (int k=A; k<=B; k++)
							if (id[k]==idi) id[k]=idj;
					}
			pw.println(res);
		}
		pw.flush();
		pw.close();
		sc.close();
	}
	
	public static void main(String[] args) throws Exception {
		(new ProblemB()).doMain();
	}
}